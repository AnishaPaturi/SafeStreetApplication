# app.py

import torch
from PIL import Image
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from flask import Flask, request, jsonify
from flask_cors import CORS
import io
from torchvision import transforms

# Set device
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

# Load model and processor
processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-flan-t5-xl",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
).to(device)

# 🔥 Warm up model
with torch.no_grad():
    dummy_image = Image.new('RGB', (512, 512), color='white')
    dummy_inputs = processor(images=dummy_image, return_tensors="pt", padding=True).to(device)
    _ = model.generate(**dummy_inputs)

# 📸 Caption generator
def generate_caption(image):
    image = preprocess_image(image)

    inputs = processor(images=image, text="Is this a road? Describe its condition in detail.", return_tensors="pt").to(device)

    with torch.no_grad():
        output = model.generate(**inputs, max_length=100, num_beams=5)

    caption = processor.tokenizer.decode(output[0], skip_special_tokens=True).strip()
    return caption or "[No caption generated]"

def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize(512),
        transforms.CenterCrop(512),
    ])
    return transform(image.convert("RGB"))

# 📋 Caption analyzer
def generate_summary(caption):
    caption_lower = caption.lower()

    likely_road_context = ["road", "street", "lane", "highway", "vehicles", "cars", "bikes", "traffic", "sidewalk", "intersection", "pothole", "muddy surface"]
    is_road = any(keyword in caption_lower for keyword in likely_road_context)

    if not is_road:
        return "Image might not be recognized as a road scene. Please verify manually.", "N/A", "N/A"

    if any(word in caption_lower for word in ["pothole", "hole", "pit", "depression"]):
        return "Pothole detected", "High", "Urgent"
    elif any(word in caption_lower for word in ["crack", "split", "fracture"]):
        return "Crack detected", "Medium", "Moderate"
    elif any(word in caption_lower for word in ["debris", "rock", "obstruction", "stone"]):
        return "Debris on road", "Low", "Moderate"
    elif any(word in caption_lower for word in ["damaged", "broken", "collapsed", "blocked"]):
        return "Roadblock or severe damage", "High", "Critical"
    elif "no damage" in caption_lower or "clear road" in caption_lower:
        return "No damage detected", "None", "None"
    else:
        return "Road detected, but unclear type of damage", "Unknown", "Review needed"

# 🌐 Flask setup
app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    try:
        image = Image.open(io.BytesIO(request.files['image'].read())).convert("RGB")

        caption = generate_caption(image)
        damage_type, severity, priority = generate_summary(caption)

        return jsonify({
            'caption': caption,
            'summary': f"{damage_type}. Severity: {severity}. Priority: {priority}.",
            'damage_type': damage_type,
            'severity': severity,
            'priority': priority
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # Run on all interfaces so you can access via local network IP
    app.run(host="0.0.0.0", port=5000)

!pip install flask pyngrok transformers torch torchvision pillow -q
import os
import io
import time
import threading
from flask import Flask, request, jsonify
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
from pyngrok import ngrok, conf

# Set ngrok auth token
conf.get_default().auth_token = "2wbtqVs3HMZ30vRPHOaEXCoCl1N_6fECZVixiuLq7YF7bchYY"

# Kill any previous tunnels
ngrok.kill()

# Start Flask app
app = Flask(__name__)

# Load model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

labels = [
    "a road with potholes",
    "a cracked road surface",
    "a road with waterlogging",
    "a clean road in good condition",
    "a road with debris or garbage",
    "a severely damaged road"
]

summary_map = {
    "a road with potholes": ("Pothole detected", "High", "Urgent"),
    "a cracked road surface": ("Crack detected", "Medium", "Moderate"),
    "a road with waterlogging": ("Waterlogging", "Medium", "High"),
    "a clean road in good condition": ("No damage detected", "None", "None"),
    "a road with debris or garbage": ("Debris on road", "Low", "Moderate"),
    "a severely damaged road": ("Severe damage", "High", "Critical")
}

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    try:
        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        inputs = processor(text=labels, images=image, return_tensors="pt", padding=True).to(device)

        with torch.no_grad():
            outputs = model(**inputs)
            probs = outputs.logits_per_image.softmax(dim=1).squeeze()

        best_idx = torch.argmax(probs).item()
        best_label = labels[best_idx]
        damage_type, severity, priority = summary_map[best_label]

        return jsonify({
            'label': best_label,
            'summary': f"{damage_type}. Severity: {severity}. Priority: {priority}.",
            'confidence': f"{probs[best_idx].item():.2f}"
        })

    except Exception as e:
        return jsonify({'error': 'Failed to analyze image', 'details': str(e)}), 500

# Start server with ngrok
public_url = ngrok.connect(5000)
print("🚀 Public URL:", public_url)

def run_app():
    app.run(host="0.0.0.0", port=5000)

thread = threading.Thread(target=run_app)
thread.start()

# Wait a bit for server to start
time.sleep(5)

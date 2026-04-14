import os
import io
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

# -------------------------------
# Flask App Setup
# -------------------------------
app = Flask(__name__)
CORS(app)

# -------------------------------
# Device (FORCE CPU for Render)
# -------------------------------
device = "cpu"

# -------------------------------
# Load Model (with caching)
# -------------------------------
MODEL_NAME = "openai/clip-vit-base-patch32"
CACHE_DIR = "./models"

print("🔄 Loading model...")

model = CLIPModel.from_pretrained(
    MODEL_NAME,
    cache_dir=CACHE_DIR
).to(device)

processor = CLIPProcessor.from_pretrained(
    MODEL_NAME,
    cache_dir=CACHE_DIR
)

model.eval()

print("✅ Model loaded successfully!")

# -------------------------------
# Labels
# -------------------------------
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

# -------------------------------
# Health Check Route
# -------------------------------
@app.route("/")
def home():
    return "🚀 AI Service is running!"

# -------------------------------
# Analyze Route
# -------------------------------
@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']

    try:
        image = Image.open(io.BytesIO(file.read())).convert("RGB")

        # -------------------------------
        # Step 1: Check if it's a road
        # -------------------------------
        road_labels = [
            "a road", "a street", "a highway",
            "a paved road", "an asphalt road",
            "not a road"
        ]

        road_inputs = processor(
            text=road_labels,
            images=image,
            return_tensors="pt",
            padding=True
        ).to(device)

        with torch.no_grad():
            road_outputs = model(**road_inputs)
            road_probs = road_outputs.logits_per_image.softmax(dim=1).squeeze()

        is_road_confidence = sum(
            road_probs[i].item() for i in range(len(road_labels) - 1)
        )

        if is_road_confidence < 0.5:
            return jsonify({
                'label': "Unrelated image",
                'summary': "The uploaded image does not appear to be of a road.",
                'confidence': f"{is_road_confidence:.2f}"
            })

        # -------------------------------
        # Step 2: Damage Classification
        # -------------------------------
        inputs = processor(
            text=labels,
            images=image,
            return_tensors="pt",
            padding=True
        ).to(device)

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
        return jsonify({
            'error': 'Failed to analyze image',
            'details': str(e)
        }), 500

# -------------------------------
# Run App (Render Compatible)
# -------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
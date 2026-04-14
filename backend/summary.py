# Removed ngrok installation comment
import os
import io
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

# Start Flask app
app = Flask(__name__)
CORS(app)

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

        # First, check if the image is of a road
        road_labels = ["a road", "a street", "a highway", "a paved road", "an asphalt road", "not a road"]
        road_inputs = processor(text=road_labels, images=image, return_tensors="pt", padding=True).to(device)

        with torch.no_grad():
            road_outputs = model(**road_inputs)
            road_probs = road_outputs.logits_per_image.softmax(dim=1).squeeze()

        is_road_confidence = sum(road_probs[i].item() for i in range(len(road_labels) - 1))  # sum of road-related labels
        not_road_confidence = road_probs[-1].item()

        if is_road_confidence < 0.5:  # Lowered threshold to 0.5
            return jsonify({
                'label': "Unrelated image",
                'summary': "The uploaded image does not appear to be of a road.",
                'confidence': f"{is_road_confidence:.2f}"
            })

        # Now do the actual road damage classification
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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


#####for testing with a single file 
# from google.colab import files
# import requests

# # Upload an image from your device
# uploaded = files.upload()
# img_path = list(uploaded.keys())[0]

# # Set your ngrok public URL (copy from Cell 2)
# url = "https://f354-34-80-3-91.ngrok-free.app/analyze"  # Replace this!

# with open(img_path, 'rb') as f:
#     files = {'image': f}
#     response = requests.post(url, files=files)
#     print("🔍 Response:", response.json())

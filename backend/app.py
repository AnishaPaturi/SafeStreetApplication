from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Configure Gemini API
API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyDhwvFqCQ-mdtFCG6vwCAFZItb2IQBtDPU')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# Existing routes (e.g., login, signup, upload)
@app.route('/api/auth/login', methods=['POST'])
def login():
    # Your existing login logic
    pass

@app.route('/api/upload/new', methods=['POST'])
def upload():
    # Your existing upload logic
    pass

# Add chatbot route
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('question', '')
        if not user_input:
            return jsonify({'error': 'No question provided'}), 400

        chat = model.start_chat(history=[])  # Add history if needed
        response = chat.send_message(user_input)
        return jsonify({'answer': response.text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
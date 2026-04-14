<div align="center">
  <h1>🚦 Safe-Street</h1>
  <p><b>AI-powered Damage Detection & Road Maintenance Application</b></p>
  
  ![React Native](https://img.shields.io/badge/React%20Native-000000?style=for-the-badge&logo=react&logoColor=61DAFB)
  ![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
  ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
  ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
</div>

---

## 🌟 Overview
**SafeStreet** streamlines road maintenance by leveraging modern mobile technology and Artificial Intelligence. The platform features an intuitive mobile application for field reporting, integrating an advanced ViT (Vision Transformer) model to classify damage and assess severity. It provides authorities with an interactive dashboard, automatic email reporting, and AI-generated insights via a seamless modern architecture.

## 🚀 Key Features
- **Intelligent Damage Detection**: Native ViT machine learning models automatically evaluate uploaded road conditions.
- **Cross-Platform Mobile Application**: Robust reporting interface allowing users to upload images and automatically geolocate issues.
- **Automated Summaries**: Python-backed analysis generates damage summaries and pushes alerts to supervisors.
- **Comprehensive Dashboard**: View outstanding reports, download automatically generated PDFs, and manage resolutions.

## 🛠️ Technology Stack
* **Frontend**: React Native, Expo, React Navigation
* **Mobile API (Backend)**: Express.js, Node.js, MongoDB, Mongoose
* **Machine Learning API**: Python, Flask, PyTorch, Transformers

---

## 💻 Getting Started

Follow these steps to set up the project locally on your machine.

### 1. Prerequisites
- Node.js
- Python 3.9+
- Expo CLI
- Ngrok (or any local tunneling software)

### 2. Local Installation

Clone the repository and install dependencies for both the frontend and backend:

```bash
# Install frontend dependencies
npm install

# Navigate to backend and install Node dependencies
cd backend
npm install
```

### 3. Environment Configuration
To run the project, you must set up your backend servers and tunnel them to the web. The application is completely centralized to pull configuration strictly from `app.config.js`.

1. **Start the Node Server**:
   ```bash
   cd backend
   npm start
   ```
2. **Start the Flask AI Service**:
   ```bash
   cd backend
   python summary.py
   ```
3. **Tunneling**: 
   Since the React Native app requires access to your local machine, use `ngrok` to expose both services:
   ```bash
   ngrok http 5000 # For Flask App
   ngrok http 3000 # For Node server
   ```

4. **Update `app.config.js`**:
   Copy the `ngrok-free.app` URLs from your tunnels and paste them directly into your frontend configuration:
   ```javascript
   export default {
     expo: {
       extra: {
         MOBILE_API_URL: 'https://<your-node-ngrok>.ngrok-free.app',
         FLASK_API_URL: 'https://<your-flask-ngrok>.ngrok-free.app'
       }
     }
   }
   ```

### 4. Run the Application
Start the Expo server and scan the QR code to test on your phone.
```bash
npm start
```

---
> *Safe-Street is an ongoing project engineered to modernize infrastructure management.*

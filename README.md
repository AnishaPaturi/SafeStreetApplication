<div align="center">
  <h1>🚦 SafeStreet</h1>
  <p><b>AI-Powered Damage Detection & Proactive Road Maintenance Platform</b></p>
  
  ![React Native](https://img.shields.io/badge/React%20Native-000000?style=for-the-badge&logo=react&logoColor=61DAFB)
  ![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
  ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
  ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
</div>

---

## 🌟 Overview
Traditional road maintenance has long been a slow and reactive process, heavily dependent on manual inspections and citizen complaints. This approach often results in delays that lead to higher costs, deteriorating road conditions, and increased accident risks. 

**SafeStreet** addresses these challenges head-on by leveraging cutting-edge Artificial Intelligence to revolutionize infrastructure maintenance. Our platform instantly detects road damage using AI, enabling real-time reporting that speeds up repair processes and smartly prioritizes urgent issues before they become severe. The business problem tackled by SafeStreet is clear: slow inspections are replaced by instant AI detection, delayed repairs are prioritized intelligently through automated reporting, and lacking visibility is solved with a real-time dashboard.

## 🚀 Key Features & Workflow
1. **Intelligent Damage Detection**: Hugging Face Vision Transformer (ViT) models automatically evaluate uploaded road conditions and classify defects ranging from potholes to severe cracking.
2. **Cross-Platform Mobile Application**: A robust reporting interface allowing field workers and citizens to upload images, auto-fill geographic location data, and context immediately.
3. **Automated Analysis & OTP Security**: Python-backed analysis generates dynamic PDF damage summaries. The platform secures internal logins through OTP email verification workflows.
4. **Comprehensive Dashboard**: Supervisors can view the queue of outstanding reports, track resolution statuses in real-time, and download automatically generated PDFs.

## 🧠 Machine Learning Architecture
At the heart of the system is the AI model, a powerful **Vision Transformer (ViT)**, which excels at complex image classification tasks. 
* **Dataset Engineering**: We custom-built a labeled dataset of real-world images representing potholes, cracks, and road defects. 
* **Augmentation**: To ensure robust generalization against diverse weather and lighting conditions, the dataset was supplemented with Kaggle's Road Damage Detection (RDD) dataset.
* **Preprocessing**: Strict pipelines for quality checks, standardizing image sizes and color formats, alongside strategic data augmentation to ensure real-world adaptability without overfitting.

## 🛠️ Technology Stack
* **Frontend**: React Native, Expo, React Navigation, React.js
* **Mobile API (Backend Component)**: Express.js, Node.js, MongoDB, Mongoose
* **Machine Learning API Component**: Python, Flask, PyTorch, Transformers, jsPDF
* **Infrastructure**: Vercel (Web / Dashboard Routing), Render (API Backend Deployment Target)

---

## 💻 Getting Started

Follow these steps to set up the project locally on your machine.

### 1. Prerequisites
- Node.js (v18+)
- Python 3.9+
- Expo CLI
- Ngrok (or any local tunneling software)

### 2. Local Installation

Clone the repository and install dependencies for both the frontend and backend architectures:

```bash
# Install Expo frontend dependencies
npm install

# Navigate to backend and install Node dependencies
cd backend
npm install
```

### 3. Environment Configuration
To run the project, you must set up your backend servers and tunnel them locally. The application is completely centralized to pull configuration strictly from `app.config.js`.

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
   Since the Expo React Native app requires access to your local machine over your phone/emulator network, use `ngrok` to expose both services:
   ```bash
   ngrok http 5000 # To expose the Flask AI Application
   ngrok http 3000 # To expose the Node Backend server
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
You will need **three terminal windows** open simultaneously to run the full stack:
1. One running the **Node API** (`npm start` inside `backend/`).
2. One running the **Flask AI Service** (`python summary.py` inside `backend/`).
3. One running the **React Native App**:
   ```bash
   npx expo start
   ```
*(Scan the QR code printed in the terminal via the Expo Go app on your iOS/Android device!)*

---

## 🔮 Future Enhancements
SafeStreet is engineered to bridge the gap between public reporting and local government action. Upcoming features include:
- **Cloud Storage Integration**: Migrating local backend image processing heavily towards AWS S3 / Cloudinary for infinite storage scale.
- **Crowdsourced Verification**: Enabling citizens to verify ("upvote") reported road damage for algorithmic priority escalation.
- **Live GPS Tracking & Clustering**: Map visualizations showing geographic hotspots of infrastructure degradation.
- **Automated Dashboard Alerts**: SMS/Email push hooks for immediate dispatch capabilities to municipal response teams.

---

## 👨‍💻 Authors
- **Anisha Paturi** - *Initial Work & Development* - [AnishaPaturi](https://github.com/AnishaPaturi)

---
> *SafeStreet — Engineering smarter, safer infrastructure through AI.*

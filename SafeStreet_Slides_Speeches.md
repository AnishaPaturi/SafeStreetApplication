# SafeStreet Presentation Speeches



## Slide 1: Scope and Business Problem Tackled

Traditional road maintenance has long been a slow and reactive process, heavily dependent on manual inspections and citizen complaints. This approach often results in delays that lead to higher costs, deteriorating road conditions, and increased accident risks. SafeStreet addresses these challenges head-on by leveraging cutting-edge AI technology to revolutionize road maintenance.

SafeStreet instantly detects road damage using AI, enabling real-time reporting that speeds up repair processes. The system smartly prioritizes urgent issues, ensuring that the most critical problems are addressed first. By providing predictive insights, SafeStreet helps prevent worsening road conditions before they become severe. This approach is not only cost-effective but also saves valuable time and resources.

The business problem tackled by SafeStreet is clear: delayed inspections and repairs lead to accidents and high maintenance costs. Traditional methods are slow and reactive, but SafeStreet’s AI detection and automated reporting enable faster, smarter road management. Slow inspections are replaced by instant AI damage detection, delayed repairs are prioritized through reporting, high costs are optimized with data insights, and lack of tracking is solved with a real-time dashboard.

---

## Slide 2: Work Flow

The SafeStreet workflow is designed to streamline the entire road damage reporting and repair process. It begins with users logging into the application, which serves both workers and supervisors. Workers upload images of road damage through the app, which are then analyzed by the AI system.

The AI analysis automatically detects and classifies the damage. Following this, the system auto-fills GPS location data and worker input to ensure accurate reporting. Workers then review and submit their reports, which are checked and sent to the appropriate authorities.

If the report is approved, it is forwarded to authorities for action; if not, it is sent back to workers for revision. Authorities receive the report and provide status updates, which workers can track in real-time through the app. This workflow ensures efficient communication and timely responses, reducing delays and improving road maintenance outcomes.

---

## Slide 3: Tech Stack and Model Dataset

SafeStreet’s technology stack is robust and modern. The frontend is built using React.js for the web and React Native for mobile, with HTML, CSS, and JavaScript forming the core technologies. The backend leverages Node.js, Express.js, and MongoDB for scalable and efficient data management.

At the heart of the system is the AI model, a Vision Transformer (ViT), which excels at image classification tasks. Deployment is handled via Vercel for the web frontend and Render for the backend. The mobile app is currently under development and not yet deployed.

The model dataset was custom-built by capturing and labeling real-world images of potholes, cracks, and other road defects. To enhance the dataset’s diversity and size, it was supplemented with the Road Damage Detection (RDD) dataset from Kaggle. This combination ensures the AI model is trained on a wide variety of conditions, improving accuracy and real-world performance. Data preprocessing steps include quality checks, standardization of image sizes and color formats, and data augmentation to improve model adaptability.

---

## Slide 4: Architectural Diagram and Deployment Strategy

The architectural design of SafeStreet integrates multiple components to deliver a seamless user experience. Users interact with the system through a mobile app built with React Native and a web dashboard built with React.js. The backend consists of a Node.js server with REST APIs, powered by Express.js, and a MongoDB database for data storage.

The AI model, based on Hugging Face’s Vision Transformer, processes images and provides damage classification. The deployment strategy involves cross-platform mobile app development with OTA updates, scalable web frontend deployment on Vercel, and backend hosting on Render with MongoDB Atlas.

Primary users of SafeStreet include maintenance teams, municipal authorities, road inspectors, government agencies, and the general public. This broad user base ensures that road damage reporting and management is accessible and effective across multiple stakeholders.

---

## Slide 5: Challenges Faced and Road Damage Detection Tool: Pros and Cons

SafeStreet faced several challenges during development. Creating dynamic PDFs for reports using jsPDF required careful implementation. Ensuring reliable automated email delivery was another hurdle. Managing multiple API endpoints efficiently was critical for smooth operation. Storing images on the backend posed storage challenges. Implementing the Vision Transformer for image classification required overcoming technical complexities. Secure OTP verification was necessary for user authentication.

The Road Damage Detection tool offers many advantages: it improves public safety through accurate AI detection, works seamlessly on web and mobile platforms, provides an easy image upload and reporting interface, enhances model generalization with diverse data, streamlines municipal responses through automation, and offers connectivity features.

However, there are some limitations: testing on mobile devices can be limited, high computational power is required for AI detection, privacy and consent issues arise with data, real-time municipal alerts are lacking, and internet connectivity is necessary for uploading images.

---

## Slide 6: Summary and Future Enhancements

In summary, SafeStreet is an AI-powered platform designed to detect and report road damages such as potholes and cracks. Users can upload real-world images via web or mobile interfaces. The system uses a Vision Transformer model for accurate classification, trained on both custom and public datasets to improve reliability.

The platform encourages contributions from civilians and municipal workers, bridging the gap between public reports and timely government action. Designed to be user-friendly and accessible, SafeStreet facilitates smoother issue reporting and enhances road safety by enabling early detection and resolution of infrastructure problems.

Future enhancements include integrating cloud storage for scalability, launching a mobile app for better accessibility, enabling crowdsourced damage verification to allow users to confirm reported issues, expanding multi-class damage detection capabilities, implementing live GPS tagging and map visualization, and providing automated alerts and dashboards for authorities to improve response times and oversight.

---

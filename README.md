MonReader: AI-Powered Document Digitization and Text-to-Speech Solution
Overview
MonReader is an innovative Artificial Intelligence and Computer Vision solution designed to digitize documents efficiently and seamlessly. Built for the blind, researchers, and individuals requiring bulk document scanning, MonReader leverages advanced machine learning techniques to provide fully automatic, high-speed, and high-quality document digitization.

Our project includes two core components:

Page Flip Detection Model: A computer vision solution predicting page-flipping actions using PyTorch.
Text-to-Speech Application: A Python application using PaddleOCR for text recognition and text-to-speech conversion, deployed on Microsoft Azure.
Features
Computer Vision Solutions:

Page flip detection using PyTorch.
High-accuracy document cropping and dewarping.
Text recognition with PaddleOCR.
Text-to-Speech Application:

Extracts text from book images and converts it to speech.
Designed for accessibility and efficiency.
Azure Deployment:

Deployed on Azure Container Apps for scalability and accessibility.
Data Description
Dataset:
We collected video data using smartphones and labeled them as flipping or not flipping. Each video was clipped into short sequences, and frames were saved with the naming convention VideoID_FrameNumber.

Dataset Details:
Videos: Clips labeled as "flipping" or "not flipping".
Frames: Sequentially saved frames extracted from the video clips.

Goal
Page Flip Detection: Predict whether an image depicts a page-flipping action.
Text-to-Speech: Enable high-quality text extraction and reading from book images.
Metrics
F1 Score: Used to evaluate model performance. A higher F1 score indicates better model performance.
Technical Challenges
Accurately detecting page-flipping actions in diverse lighting and background conditions.
Efficiently integrating PaddleOCR for text recognition and text-to-speech conversion.
Deploying the solution seamlessly on Azure while ensuring accessibility and scalability.
Page Flip Detection: Implementation Steps
1. Data Preprocessing:
Extracted frames from videos.
Resized images for uniformity.
Augmented data to improve model robustness.
2. Model Development:
Used PyTorch to build a Convolutional Neural Network (CNN) model.
Defined a binary classification task (flipping vs. not flipping).
3. Training:
Split data into training and validation sets.
Optimized the model using:
Loss Function: Binary Cross-Entropy Loss.
Optimizer: Adam.
Metrics: F1 Score.
4. Evaluation:
Evaluated the trained model on the validation dataset.
Achieved high F1 scores, demonstrating model efficacy.
5. Prediction:
Deployed the model for inference on new images to predict flipping actions.
Text-to-Speech Application: Implementation Steps
1. Text Recognition:
Integrated PaddleOCR for optical character recognition (OCR).
Preprocessed book images and extracted text.
2. Text-to-Speech Conversion:
Used gTTS (Google Text-to-Speech) to convert recognized text into audio.
3. Application Deployment:
Deployed the Python application on Microsoft Azure using Docker.
Configured Azure Container Apps to ensure scalability and accessibility.
Deployment on Microsoft Azure
Steps:
Containerization:

Built a Docker image for the Python application.
Included all dependencies (PaddleOCR, gTTS, Flask).
Push to Docker Hub:

Pushed the Docker image to Docker Hub for accessibility.
Deploy on Azure:

Used Azure Container Apps to deploy the Docker container.
Configured port mapping and ingress settings for public access.
Access:
Users can upload images through a web interface hosted on Azure. The application extracts text, converts it to speech, and provides the audio file for download.

How to Run Locally
Prerequisites:
Python 3.10 or later
PaddleOCR
PyTorch
Flask
Docker (for containerization)
Steps:
Clone the Repository:

bash
Copy code
git clone <repository_url>
cd project-directory
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
Access the App: Open your browser and navigate to http://localhost:5000.

Files
project4.ipynb: Contains the code for page flip detection using PyTorch.
app.py: Flask application for text-to-speech conversion.
Templates:
upload.html: Page for uploading book images.
result.html: Page displaying extracted text and audio download option.
Dockerfile: For containerizing the application.
Video: Demonstration of the deployed application.
Video Demonstration
The attached video demonstrates:

The text-to-speech application in action.
Deployment and usage of the Azure-hosted web app.
Future Work
Enhance the page flip detection model to support video streams directly.
Optimize PaddleOCR for faster text extraction.
Add multi-language support for text recognition and speech synthesis.
The video link that show the deployment and use of the application is:
https://youtu.be/m6m_ETYGwuM

Contact
For inquiries or collaboration, reach out at:

Email: faridshahnavaz@gmail.com
LinkedIn: www.linkedin.com/in/farid-shahnavaz

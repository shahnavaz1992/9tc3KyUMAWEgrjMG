from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from gtts import gTTS
from paddleocr import PaddleOCR
import os
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Use English OCR model

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "image" not in request.files:
            return "No file uploaded", 400

        image_file = request.files["image"]
        if image_file.filename == "":
            return "No file selected", 400

        # Save the uploaded file
        filename = secure_filename(image_file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        image_file.save(file_path)

        # Perform OCR using PaddleOCR
        try:
            result = ocr.ocr(file_path, cls=True)
            extracted_text = " ".join([line[1][0] for line in result[0]])  # Extract detected text
        except Exception as e:
            return f"Error processing image: {e}", 500

        # Convert text to speech
        try:
            tts = gTTS(extracted_text, lang="en")
            audio_path = os.path.join(app.config["UPLOAD_FOLDER"], "output.mp3")
            tts.save(audio_path)
        except Exception as e:
            return f"Error converting text to speech: {e}", 500

        return render_template("result.html", text=extracted_text, audio_path="output.mp3")

    return render_template("upload.html")


@app.route("/download_audio", methods=["GET"])
def download_audio():
    audio_path = os.path.join(app.config["UPLOAD_FOLDER"], "output.mp3")
    return send_file(audio_path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

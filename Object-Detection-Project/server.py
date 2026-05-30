from flask import Flask, request, send_file, jsonify
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np
import cv2

app = Flask(__name__)

# Load model (expects `yolov8n.pt` to be present in the project root)
model = YOLO("yolov8n.pt")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/detect", methods=["POST"])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'no image provided'}), 400

    file = request.files['image'].read()
    image = Image.open(io.BytesIO(file)).convert("RGB")
    img = np.array(image)[:, :, ::-1]  # RGB -> BGR for OpenCV

    # Run inference
    results = model(img)

    # Annotate frame
    annotated = results[0].plot()

    # Encode as JPEG and return
    success, encoded = cv2.imencode('.jpg', annotated)
    if not success:
        return jsonify({'error': 'failed to encode image'}), 500

    return send_file(io.BytesIO(encoded.tobytes()), mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

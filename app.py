from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MODEL_PATH = "model_unquant.tflite"

interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

labels = [
    "HEALTHY",
    "COMMUNIATED",
    "DISPLACED FRACTURES",
    "TRANSVERSE FRACTURES",
    "OTHER FRACTURES"
]

IMG_SIZE = 224


def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(image, dtype=np.float32)
    img_array = (img_array / 127.5) - 1
    img_array = np.expand_dims(img_array, axis=0)

    interpreter.set_tensor(
        input_details[0]["index"],
        img_array
    )

    interpreter.invoke()

    prediction = interpreter.get_tensor(
        output_details[0]["index"]
    )[0]

    predicted_index = np.argmax(prediction)

    confidence = float(
        prediction[predicted_index] * 100
    )

    probabilities = {}

    for i, label in enumerate(labels):
        probabilities[label] = round(
            float(prediction[i] * 100),
            2
        )

    return (
        labels[predicted_index],
        confidence,
        probabilities
    )


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    confidence = None
    image_file = None
    probabilities = {}

    if request.method == "POST":

        file = request.files.get("image")

        if file and file.filename != "":

            image_file = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(image_file)

            prediction, confidence, probabilities = predict_image(
                image_file
            )

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        probabilities=probabilities,
        image_file=image_file
    )
@app.route("/new_scan")
def new_scan():
    return render_template("new_scan.html")

@app.route("/scan_history")
def scan_history():
    return render_template("scan_history.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")


if __name__ == "__main__":
    app.run(debug=True)
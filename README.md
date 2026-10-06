# 🩻 AI Fracture Detection

A Flask-based web application that uses a **TensorFlow Lite model** to analyze X-ray images and classify them into different fracture categories.

## 🚀 Features

- Upload X-ray images
- AI-based fracture classification
- Prediction confidence score
- Probability for each class
- Simple Flask web interface

## 🧠 Classes

- HEALTHY
- COMMUNIATED
- DISPLACED FRACTURES
- TRANSVERSE FRACTURES
- OTHER FRACTURES

## 🛠️ Tech Stack

- Python
- Flask
- TensorFlow Lite
- NumPy
- Pillow

## 📂 Structure

```text
├── app.py
├── model_unquant.tflite
├── labels.txt
├── templates/
└── static/uploads/
```

## ▶️ Run Locally

```bash
pip install flask tensorflow numpy pillow
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## ⚠️ Disclaimer

This project is for **educational purposes only** and should not be used as a substitute for professional medical diagnosis.

---

# 🌿 Plant Disease Detection System (Deep Learning + FastAPI)

An end-to-end **Plant Disease Classification** system built using **TensorFlow (CNN)** and deployed using **FastAPI & Docker**.  
The model classifies plant leaf images into **15 disease categories** with high accuracy.

---

## 📌 Project Overview

This project covers the **complete machine learning lifecycle**:

- ✅ Data loading & preprocessing
- ✅ CNN model training & evaluation
- ✅ Model saving in Keras format
- ✅ REST API for inference (FastAPI)
- ✅ Dockerized deployment
- ✅ Production-ready structure (MLOps-friendly)

---

## 🧠 Model Details

- **Architecture:** Custom CNN
- **Input size:** `256 x 256 x 3`
- **Classes:** 15 plant disease categories
- **Framework:** TensorFlow / Keras
- **Final model format:** `.keras`

---

## 📂 Project Structure

# 🌿 Plant Disease Detection System (Deep Learning + FastAPI)

An end-to-end **Plant Disease Classification** system built using **TensorFlow (CNN)** and deployed using **FastAPI & Docker**.  
The model classifies plant leaf images into **15 disease categories** with high accuracy.

---

## 📌 Project Overview

This project covers the **complete machine learning lifecycle**:

- ✅ Data loading & preprocessing
- ✅ CNN model training & evaluation
- ✅ Model saving in Keras format
- ✅ REST API for inference (FastAPI)
- ✅ Dockerized deployment
- ✅ Production-ready structure (MLOps-friendly)

---

## 🧠 Model Details

- **Architecture:** Custom CNN
- **Input size:** `256 x 256 x 3`
- **Classes:** 15 plant disease categories
- **Framework:** TensorFlow / Keras
- **Final model format:** `.keras`

---

## 📂 Project Structure

# 🌿 Plant Disease Detection System (Deep Learning + FastAPI)

An end-to-end **Plant Disease Classification** system built using **TensorFlow (CNN)** and deployed using **FastAPI & Docker**.  
The model classifies plant leaf images into **15 disease categories** with high accuracy.

---

## 📌 Project Overview

This project covers the **complete machine learning lifecycle**:

- ✅ Data loading & preprocessing
- ✅ CNN model training & evaluation
- ✅ Model saving in Keras format
- ✅ REST API for inference (FastAPI)
- ✅ Dockerized deployment
- ✅ Production-ready structure (MLOps-friendly)

---

## 🧠 Model Details

- **Architecture:** Custom CNN
- **Input size:** `256 x 256 x 3`
- **Classes:** 15 plant disease categories
- **Framework:** TensorFlow / Keras
- **Final model format:** `.keras`

---

## 📂 Project Structure

Plant-Disease-Detection/
│
├── notebooks/
│ └── train_model.ipynb # Training & experimentation
│
├── model/
│ └── plant_disease_model.keras
│
├── app.py # FastAPI inference service
├── requirements.txt
├── Dockerfile
├── README.md


---

## 🚀 FastAPI Endpoints

### 🔍 Health Check

---
GET /health

**Response**
```json
{
  "status": "ok"
}

Predict Plant Disease
POST /predict


Request

multipart/form-data

Key: file (image file)

Response

{
  "predicted_class": "Tomato_Late_blight",
  "confidence": 0.91
}

🧪 Model Evaluation

Validation Accuracy: ~89%

Test Accuracy: ~91%

Early stopping & learning rate reduction used to prevent overfitting.

🐳 Docker Deployment
Build Docker Image
docker build -t plant-disease-api .

Run Container
docker run -p 8000:8000 plant-disease-api


API available at:

http://localhost:8000


Swagger UI:

http://localhost:8000/docs

🧰 Tech Stack

Python 3.10

- TensorFlow / Keras
- FastAPI
- Uvicorn
- Docker
- NumPy, Pillo
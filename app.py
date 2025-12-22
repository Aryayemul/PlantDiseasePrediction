import io
import numpy as np
from PIL import Image

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

import tensorflow as tf

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
MODEL_PATH = "plant_disease_model.keras"
IMAGE_SIZE = (256, 256)
CONFIDENCE_THRESHOLD = 0.6

CLASS_NAMES = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy"
]

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# --------------------------------------------------
# APP INIT
# --------------------------------------------------
app = FastAPI(title="Plant Disease Detection API")

# --------------------------------------------------
# UTILS
# --------------------------------------------------
def preprocess_image(image_bytes: bytes):
    try:
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize(IMAGE_SIZE)

        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, axis=0)

        return img_array
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

# --------------------------------------------------
# ROUTES
# --------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": True}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Only JPG/PNG images are supported")

    image_bytes = await file.read()
    img = preprocess_image(image_bytes)

    preds = model.predict(img)
    confidence = float(np.max(preds))
    class_index = int(np.argmax(preds))
    predicted_class = CLASS_NAMES[class_index]

    if confidence < CONFIDENCE_THRESHOLD:
        return JSONResponse(
            status_code=200,
            content={
                "prediction": "Uncertain",
                "confidence": confidence
            }
        )

    return {
        "prediction": predicted_class,
        "confidence": confidence
    }

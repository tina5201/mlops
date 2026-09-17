from pathlib import Path

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException

from app.schemas import HouseFeatures, PredictionResponse

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

app = FastAPI(
    title="House Price Prediction API",
    description="A simple ML inference API built with FastAPI.",
    version="1.0.0",
)

# Load the model once when the application starts.
model = joblib.load(MODEL_PATH)


@app.get("/")
def root():
    return {
        "message": "House Price Prediction API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(data: HouseFeatures):
    try:
        features = np.array(
            [[data.area, data.bedrooms, data.bathrooms, data.age]],
            dtype=float,
        )

        prediction = model.predict(features)[0]

        return {"predicted_price": float(prediction)}

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

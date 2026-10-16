
from pathlib import Path

import joblib
import numpy as np
from flask import Flask, jsonify, render_template, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

app = Flask(__name__)

# Load the trained model
model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None
    }), 200


@app.route("/prediction", methods=["POST"])
def prediction():
    try:
        data = request.get_json(silent=True)

        if data is None:
            data = request.form

        area = float(data["area"])
        bedrooms = int(data["bedrooms"])
        bathrooms = int(data["bathrooms"])
        age = int(data["age"])

        if area <= 0 or not 1 <= bedrooms <= 5:
            raise ValueError("Area must be positive and bedrooms must be 1–5.")

        if not 1 <= bathrooms <= 3 or not 0 <= age <= 30:
            raise ValueError("Bathrooms must be 1–3 and age must be 0–30.")

        features = np.array(
            [[area, bedrooms, bathrooms, age]],
            dtype=float
        )

        predicted_price = float(model.predict(features)[0])

        if request.is_json:
            return jsonify({
                "predicted_price": round(predicted_price, 2),
                "currency": "project units"
            }), 200

        return render_template(
            "index.html",
            predicted_price=round(predicted_price, 2)
        )

    except (KeyError, ValueError, TypeError) as exc:
        if request.is_json:
            return jsonify({"error": str(exc)}), 400

        return render_template(
            "index.html",
            error=str(exc)
        ), 400


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

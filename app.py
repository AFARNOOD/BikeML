from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
MODEL_PATH = "BikeML/models/bike_duration_predictor.pkl"
model = joblib.load(MODEL_PATH)

# Define the expected input features for the model
FEATURES = [
    "max_temp_c", "min_temp_c", "total_precip_mm", "snow_on_grnd_cm",
    "spd_of_max_gust_kmh", "temp_range_c", "is_rainy", "is_snowy",
    "start_hour", "start_weekday", "is_weekend"
]

@app.route("/", methods=["GET"])
def home():
    """Basic route to check if the API is running."""
    return jsonify({"message": "BikeML API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    """Prediction endpoint for the API."""
    try:
        # Parse input JSON data
        data = request.get_json()

        # Check if all required features are in the input
        missing_features = [f for f in FEATURES if f not in data]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400

        # Convert input JSON into a DataFrame
        input_data = pd.DataFrame([data])

        # Make predictions
        prediction = model.predict(input_data)[0]

        # Create a response dictionary
        response = {"predicted_duration_sec": round(prediction, 2)}
        return jsonify(response)

    except Exception as e:
        # Handle errors and return an error message
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app on localhost at port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)

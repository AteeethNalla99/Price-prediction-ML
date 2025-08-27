from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes and all origins

util.load_saved_artifacts()

@app.route("/get_location_names")
def get_location_names():
    return jsonify({
        "locations": util.get_location_names()
    })

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    return jsonify({
        "estimated_price": util.get_estimated_price(location, total_sqft, bhk, bath)
    })

if __name__ == "__main__":
    print("Starting Python flask server for Home Price Predictions.")
    app.run()
import logging
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        logging.debug("Received GET request to fetch location names")
        locations = util.get_location_names()
        response = jsonify({'locations': locations})
        response.headers.add('Access-Control-Allow-Origin', '*')
        logging.debug("Sending location names response: %s", locations)
        return response
    except Exception as e:
        logging.error("An error occurred while fetching location names: %s", str(e))
        return jsonify({'error': 'An error occurred while fetching location names'}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        location = request.form['location']
        
        logging.debug("Received POST request to predict home price: total_sqft=%s, bhk=%s, bath=%s, location=%s",
                      total_sqft, bhk, bath, location)
        
        estimated_price = util.predict_price(location, total_sqft, bath, bhk)
        
        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        logging.debug("Predicted home price: %s", estimated_price)
        return response
    except Exception as e:
        logging.error("An error occurred while predicting home price: %s", str(e))
        return jsonify({'error': 'An error occurred while predicting home price'}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=5000)

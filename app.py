from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        stock_features = data.get('features')
        if not stock_features or len(stock_features) != 4:
            return jsonify({'error': 'Invalid input, expected four features'}), 400
        predicted_price = model.predict([stock_features])[0]
        return jsonify({'predicted_price': predicted_price})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

# Stock Prediction using Python and AI

This project is a Flask-based web application for predicting stock prices using machine learning. It utilizes a linear regression model trained with historical stock data, capable of predicting the closing price from input features like opening price, high, low, and trading volume of the day

## Technology Stack

- **Python 3**: Main programming language.
- **Flask**: Framework for creating the web server.
- **scikit-learn**: Used for implementing the machine learning model.
- **yfinance**: Provides historical stock data.
- **Joblib**: Used for saving and loading the trained model.

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/amine-el-amrani/Stock-Prediction-using-Python-and-AI.git
cd Stock-Prediction-using-Python-and-AI
```

2. Environment Setup

```bash
python3 -m venv ~/.local/venv_stock
source ~/.local/venv_stock/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```
## Model Training

To train the model and create the model.pkl file, run:

```bash
python3 train_model.py
```

## Launch the Server
To start the Flask server, run:

```bash
python3 app.py
```

## Testing the Application

To test the application's prediction capabilities:
1. Set the method to POST.
2. Use the URL: http://127.0.0.1:5000/predict
3. Set the request body as JSON:
```bash
{
  "features": [183.42, 184.8, 181.66, 55630000]
}
```
Send the request and you should receive a predicted stock price as the response.


## Contributing

Contributions are welcome! Please feel free to submit pull requests, open issues, or provide feedback on how to improve the project.
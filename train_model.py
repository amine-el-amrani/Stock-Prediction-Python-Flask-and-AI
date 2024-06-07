import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def fetch_and_process_stock_data(symbol):
    stock_data = yf.download(symbol, start='2020-01-01', end='2024-02-18')
    stock_data_cleaned = stock_data.dropna()
    return stock_data_cleaned

def train_and_save_model(data):
    X = data[['Open', 'High', 'Low', 'Volume']]
    y = data['Close']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, 'model.pkl')

if __name__ == '__main__':
    stock_data_cleaned = fetch_and_process_stock_data('AAPL')
    train_and_save_model(stock_data_cleaned)

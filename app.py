from flask import Flask, jsonify
import yfinance as yf
from analysis import get_market_analysis

app = Flask(__name__)

@app.route('/get-signal/<symbol>')
def get_signal(symbol):
    # Live market data fetch karna
    data = yf.download(symbol, period="1d", interval="1m")
    analysis = get_market_analysis(data)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)
  

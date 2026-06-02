import pandas_ta as ta

def get_market_analysis(df):
    # Layer 1: EMA Filter (Trend)
    ema200 = df['close'].rolling(200).mean()
    layer1 = df['close'].iloc[-1] > ema200.iloc[-1]
    
    # Layer 2: RSI Filter (Overbought/Oversold)
    rsi = ta.rsi(df['close'], length=14)
    layer2 = rsi.iloc[-1] < 70 and rsi.iloc[-1] > 30
    
    # Layer 3-6: Yahan aap apne custom indicators add karenge
    # Jaise: Support/Resistance, Volume, Stochastic, Bollinger Bands
    
    # Simple example output
    return {
        "trend": "Bullish" if layer1 else "Bearish",
        "signal": "CALL" if (layer1 and layer2) else "PUT",
        "probability": 75 
    }

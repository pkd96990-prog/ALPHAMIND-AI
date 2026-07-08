import yfinance as yf


def get_stock_data(ticker):

    stock = yf.Ticker(ticker)

    history = stock.history(period="1mo")

    info = stock.info

    return {
        "history": history,
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE")
    }
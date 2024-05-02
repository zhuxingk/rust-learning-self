import yfinance as yf

# 获取工业富联股票实时数据
stock = yf.Ticker("601138.SS")
stock_data = stock.history(period="1d")
print(stock_data)

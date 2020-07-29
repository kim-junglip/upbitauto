import talib as ta
import matplotlib.pyplot as plt
plt.style.use('bmh')
import yfinance as yf
aapl = yf.download('AAPL', '2019-1-1','2019-12-27')
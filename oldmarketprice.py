import pyupbit

btc = pyupbit.get_ohlcv("KRW-BTC")
low = btc['low']
print(low)
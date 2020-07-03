import pyupbit

btc = pyupbit.get_ohlcv("ALL")
low = btc['low']
print(low)
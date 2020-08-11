import pandas as pd
import pyupbit
import numpy
import talib.abstract as ta
import talib

df = pyupbit.get_ohlcv("KRW-BTC")

high = df['high']
low = df['low']
close = df['close']

rsi = ta.RSI(close, timeperiod=60)

print(rsi[-1])


slowk, slowd = ta.STOCH(high, low, close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

print(slowk[-1])
print(slowd[-1])
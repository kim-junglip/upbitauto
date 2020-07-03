import pyupbit

df = pyupbit.get_ohlcv("KRW-XRP", "minute60")
how = {'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last',
       'volume': 'sum'}
df = df.resample('D').apply(how)
print(df)
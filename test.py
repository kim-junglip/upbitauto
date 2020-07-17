import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-WAXP")
    #df = df['2020']
df['range'] = (df['high'] - df['low'])
df['target'] = df['open'] + df['range'].shift(1)#1행을 내려준다.

fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],df['close'] / df['target'] - fee,1)


    #df.to_excel("upbit5.xlsx")

ror = df['ror'].cumprod()[-2]
print(ror)



df = pyupbit.get_ohlcv("KRW-WAXP")
df['range'] = (df['high'] - df['low'])
df['target'] = df['open'] + df['range'].shift(1)
fee = 0.0032
df['ror'] = np.where(df['high'] > df['target'],df['close'] / df['target'] - fee, 1)
df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

print(df['dd'].max(0))



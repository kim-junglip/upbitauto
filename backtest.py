import pyupbit
import numpy as np

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-WAXP")
    #df = df['2020']
    df['range'] = (df['high'] - df['low'])
    df['target'] = df['open'] + df['range'].shift(1)#1행을 내려준다.

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],df['close'] / df['target'] - fee,1)


    #df.to_excel("upbit5.xlsx")

    ror = df['ror'].cumprod()[-2]

    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" %(k, ror))

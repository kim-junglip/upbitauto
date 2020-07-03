import pyupbit
import numpy as np

def get_MDD(k=0.5):
    df = pyupbit.get_ohlcv("KRW-WAXP")
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)
    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],df['close'] / df['target'] - fee, 1)
    df['hpr'] = df['ror'].cumprod()
    df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100



    return df


for k in np.arange(0.1, 1.0, 0.1):
    df = get_MDD(k)
    print("%.1f, %f" % (k, df['dd'].max()))
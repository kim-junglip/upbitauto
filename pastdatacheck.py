import pyupbit

#df = pyupbit.get_ohlcv("KRW-BTC")                                                                                       #과거 시가, 고가, 저가, 종가, 거래량을 가지고온다.
df = pyupbit.get_ohlcv("ALL", count=5)                                                                              #5일간의 데이터만 조회한다.
print(df)
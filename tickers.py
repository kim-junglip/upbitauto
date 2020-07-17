import pyupbit

#tickers = pyupbit.get_tickers()                                                                                        #업비트에 있는 모든 코인 티커를 불러온다
tickers = pyupbit.get_tickers(fiat="KRW")                                                                               #업비트에 있는 원화로 거래 가능한 티커를 불러온다.
print(tickers)

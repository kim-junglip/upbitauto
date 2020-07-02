import pyupbit
import time
import datetime


with open("upbit.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    upbit = pyupbit.Upbit(key, secret)

'''
내 잔고 조회
'''
upbit = pyupbit.Upbit(key, secret)
print(upbit.get_balances())

'''
지정가 주문
'''
ret = upbit.buy_limit_order("KRW-BTC", 100, 20)
'''
변동성 돌파 목표가 계산을 위한 함수
'''
def get_target_price(ticker):#재사용을 위해 함수 선언
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]#끝에서 2번째인 전일 데이터를 가지고 온다.

    today_open = yesterday['close']#당일 시가를 얻어온다.
    yesterday_high = yesterday['high']#전일 고가를 얻어온다.
    yesterday_low = yesterday['low']#전일 저가를 얻어온다.
    target = today_open + (yesterday_high - yesterday_low) * 0.5#변동성 돌파 목표가 계산
    return target

'''
매수 함수
'''
def buy_crypto_currency(ticker):
    krw = upbit.get_balances(ticker)[2]
    orderbook = pyupbit.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw / float(sell_price)
    upbit.buy_limit_order(ticker, unit)

'''
매도 함수
'''
def sell_crypto_currency(ticker):
    unit = upbit.get_balances()
    upbit.sell_limit_order(ticker, unit)

'''
현재 시간 구하기
'''
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("KRW-BTC")

'''
매일 정각이 되면 목표가를 계산하여 갱신

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.delta(seconds=10):#00시를 초단위로 정확하게 알지 못하기 떄문에 10초의 범위안에서 실행하게 한다.
        target_price = get_target_price("KRW-BTC")
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
        sell_crypto_currency("KRW-BTC")

    current_price = pyupbit.get_current_price("KRW-BTC")
    if current_price > target_price:
        buy_crypto_currency("KRw-BTC")


    time.sleep(1)
'''

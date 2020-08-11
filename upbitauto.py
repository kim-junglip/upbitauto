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
변동성 돌파 목표가 계산을 위한 함수
'''
def get_target_price(ticker):#재사용을 위해 함수 선언
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]#끝에서 2번째인 전일 데이터를 가지고 온다.
    today_open = yesterday['close']#당일 시가를 얻어온다.
    yesterday_high = yesterday['high']#전일 고가를 얻어온다.
    yesterday_low = yesterday['low']#전일 저가를 얻어온다.
    target = today_open + (yesterday_high - yesterday_low)#변동성 돌파 목표가 계산
    return target

'''
매수 함수
'''
def buy_crypto_currency(ticker):
    krw = upbit.get_balances(ticker)[2]#내 잔고 조회
    #orderbook = pyupbit.get_orderbook(ticker)#최우선 매도 호가 조회
    #sell_price = orderbook['asks'][0]['price']#asks(매도호가) [0](첫번째) price(가격)
    #unit = krw / float(sell_price) #내 잔고 / 첫번째 매도 호가
    upbit.buy_market_order(ticker, 10000)#해당 코인을 시장가로 매수

'''
매도 함수
'''
def sell_crypto_currency(ticker):
    unit = upbit.get_balances()
    upbit.sell_market_order(ticker, unit)#해당 코인을 시장가로 매매

'''
매일 정각이 되면 목표가를 계산하여 갱신
'''
while True:
    try:
        now = datetime.datetime.now()#현재 시간 조회
        mid = datetime.datetime(now.year, now.month, now.day, 9)  # 오전 9시를 고정으로 잡는다.
        if mid < now < mid + datetime.delta(seconds=10):#00시를 초단위로 정확하게 알지 못하기 떄문에 10초의 범위안에서 실행하게 한다.
            sell_crypto_currency("KRW-BTC")#모든 코인을 매도
            target_price = get_target_price("KRW-BTC")#목표가 계산


        current_price = pyupbit.get_current_price("KRW-BTC")#현재가 조회
        if current_price > target_price:#현재가가 목표가보다 높은지 검사
            buy_crypto_currency("KRW-BTC")#매수
    except:
        print("에러 발생")
        time.sleep(1)


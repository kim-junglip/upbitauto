import pyupbit
import time
import datetime

'''
while True:#24시간 현재가를 알기위하여 무한 루프로 while을 사용
    price = pyupbit.get_current_price("KRW-BTC")#비트코인의 현재가를 가지고 온다.
    print(price)
    time.sleep(0.2)#초당 호출이 정해져 있어서 0.2초 쉰다.
'''

'''
df = pyupbit.get_ohlcv("KRW-BTC")#시가,고가,저가,종가,거래량을 가지고 온다.
print(df.tail())#최근 5개의 데이터만 가지고 온다.
'''
'''
dt = datetime.datetime(2018, 12, 1)#datetime 클래스의 초기화자로 년/월/일 을 전달한다.
now = datetime.datetime.now()#현재 시간 구하기
print(now)
#print(dt)
#print(dt.year, dt.month, dt.day)
print(now == dt)
print(now > dt)
'''
'''
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)#00:00:00 초의 datetime객체를 생성하고 1일을 더해 다음날 자정으로 만든다.
print(now)
print(mid)
'''

def get_target_price(ticker):#재사용을 위해 함수 선언
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]#끝에서 2번째인 전일 데이터를 가지고 온다.

    today_open = yesterday['close']#당일 시가를 얻어온다.
    yesterday_high = yesterday['high']#전일 고가를 얻어온다.
    yesterday_low = yesterday['low']#전일 저가를 얻어온다.
    target = today_open + (yesterday_high - yesterday_low) * 0.5#변동성 돌파 목표가 계산
    return target

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
target_price = get_target_price("KRW-BTC")

while True:
    now = datetime.datetime.now()
    if mid < now < mid + datetime.delta(seconds=10):#00시를 초단위로 정확하게 알지 못하기 떄문에 10초의 범위안에서 실행하게 한다.
        print("정각입니다")
        now = datetime.datetime.now()
        mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

    current_price = pyupbit.get_current_price("KRW-BTC")
    print(current_price)

    time.sleep(1)


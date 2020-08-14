import datetime
import time
import pyupbit
import json
import numpy as np
import backtrader as bt
from pandas import Series
from pandas import DataFrame
import math


'''
계좌 정보
'''
with open("upbit.txt") as f:
    lines = f.readlines()
    key = lines[0].strip() #1번째 줄
    secret = lines[1].strip() #2번째 줄
    upbit = pyupbit.Upbit(key, secret)


'''
거래량 상위 10위 걸러내기
'''
def firstfilter() :#첫번째 필터로 거래량 상위 10위까지 걸러낸다.
    coin = pyupbit.get_tickers(fiat="KRW")#코인 이름 불러오기
    tikervolume ={}#딕셔너리 초기화

    for i in range(len(coin)):
        try:#예외처리
            df = pyupbit.get_ohlcv(coin[i], count=1)#코인 고,저,종,거래량 불러오기
            tiker = coin[i]#코인 이름을 담는다
            volumeup = df['volume']#거래량만 담는다.
            tikervolume[tiker] = int(volumeup)#key = tiker : value = volumeup
        except Exception as x:
            pass
    VolumeAscendingOrder = sorted(tikervolume.items(), key=lambda x: x[1])#거래량 기준 오름차순
    ten = VolumeAscendingOrder[-10:]
    vo = dict(ten) #딕셔너리 형식으로 넘겨준다.
    return list(vo.keys()) #키값만 뽑아서 리스트 형식으로 넘긴다.

'''
변동성 돌파 목표가 계산을 위한 함수
'''
def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]#끝에서 2번째인 전일 데이터를 가지고 온다.
    today_open = yesterday['close']#당일 시가를 얻어온다.
    yesterday_high = yesterday['high']#전일 고가를 얻어온다.
    yesterday_low = yesterday['low']#전일 저가를 얻어온다.
    target = today_open + (yesterday_high - yesterday_low)*0.5#변동성 돌파 목표가 계산
    return target

'''
내 계좌에 있는 코인의 이름만 가지고 나온다
'''
def My_Account():
    krw = []
    krw_1 = []
    for i in range(len(upbit.get_balances()[0])) :
        krw_1.append(upbit.get_balances()[0][i]) #내 잔고 조회
        krw.append("KRW-" + krw_1[i].get('currency'))
    return krw

while True :
    try :
        '''
        거래량 기준 상위 코인 변동성 돌파로 매수
        '''
        FirstfilterList = firstfilter() #속도를 위해 모든 값을 넘겨준다
        for i in range(len(firstfilter())-1,0,-1) :
            j = FirstfilterList[i] # 상위 10개의 코인을 하나씩 j에 넣는다.
            if My_Account().count(j) == 0 : #내 계좌에 있는 코인과 비교한다.
                coin = FirstfilterList[i] #순서대로 넘겨준다.
                target_price = get_target_price(coin)
                print(coin, target_price)
                current_price = pyupbit.get_current_price(coin) #현재가 조회
                if current_price > target_price:
                    upbit.buy_market_order(coin, 5000)
                    print("매수 완료")
        '''
        오전 9시가 되면 계좌에 있는 모든 코인 소멸
        '''
        now = datetime.datetime.now()#현재 시간 조회
        mid = datetime.datetime(now.year, now.month, now.day, 9)  # 오전 9시를 고정으로 잡는다.
        if mid < now < mid + datetime.timedelta(seconds=10):
            krw_1 = []
            krw_cur = []
            krw_bal = []
            total = []
            for i in range(len(upbit.get_balances())) :
                krw_1.append(upbit.get_balances()[0][i+1])
                krw_cur.append("KRW-" + krw_1[i].get('currency'))
                krw_bal.append(krw_1[i].get('balance'))
                total = krw_cur, krw_bal
                upbit.sell_market_order(total[0][i], total[1][i])#해당 코인을 시장가로 매도
    except :
        print("에러 발생")
        time.sleep(1)






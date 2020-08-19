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
def get_target_price(ticker):#재사용을 위해 함수 선언
    df = pyupbit.get_ohlcv(ticker)
    yesterday = df.iloc[-2]#끝에서 2번째인 전일 데이터를 가지고 온다.
    today_open = yesterday['close']#당일 시가를 얻어온다.
    yesterday_high = yesterday['high']#전일 고가를 얻어온다.
    yesterday_low = yesterday['low']#전일 저가를 얻어온다.
    target = today_open + (yesterday_high - yesterday_low)#변동성 돌파 목표가 계산
    return target

def buy_crypto_currency():
    krw = []
    krw_1 = []
    for i in range(len(upbit.get_balances())) :
        krw_1.append(upbit.get_balances()[0][i+1]) #내 잔고 조회
        #coin = krw[i].get('currency')
        #krw = "KRW-" + krw_1[i].get('currency')
        krw.append("KRW-" + krw_1[i].get('currency'))
        #krw_n.append(krw[i].get('currency'))
    return krw
    #orderbook = pyupbit.get_orderbook(ticker)#최우선 매도 호가 조회
    #sell_price = orderbook['asks'][0]['price']#asks(매도호가) [0](첫번째) price(가격)
    #unit = krw / float(sell_price) #내 잔고 / 첫번째 매도 호가
    #upbit.buy_market_order(ticker, 10000)#해당 코인을 시장가로 매수


FirstfilterList = firstfilter() #속도를 위해 모든 값을 넘겨준다

for i in range(len(firstfilter())) :
    j = FirstfilterList[i]
    print(j)
    if buy_crypto_currency().count(j) == 1 :
        coin = FirstfilterList[i] #순서대로 넘겨준다.
        current_price = pyupbit.get_current_price(coin) #현재가 조회

        print(coin,current_price)

#print(len(upbit.get_balances()))
#print(upbit.get_balances())
#print(firstfilter())
#print(FirstfilterList)
print(buy_crypto_currency())






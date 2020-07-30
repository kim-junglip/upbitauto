import pyupbit
from pandas import Series
from pandas import DataFrame
import math

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
    vo = sorted(tikervolume.items(), key=lambda x: x[1])#거래량 기준 오름차순
    return vo[-10:]
    #print(vo[-10:])
print(firstfilter())




#close = df['close']

#vo = volume.sort_values(ascending=False)



#print(close[-5:-1])
#print(vo)
#print(vo[-1])
#print(df[-1:])



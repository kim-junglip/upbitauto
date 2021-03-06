import pyupbit
import talib.abstract as ta
import time
import math
with open("upbit.txt") as f:
    lines = f.readlines()
    key = lines[0].strip() #1번째 줄
    secret = lines[1].strip() #2번째 줄
    upbit = pyupbit.Upbit(key, secret)

coin_buy = pyupbit.get_tickers(fiat="KRW") # 코인 이름 불러오기

while True :
    cci_total_today_buy = []
    cci_total_yesterday_buy = []

    df_sell = []
    print("START")
    try :
        for i in range(len(coin_buy)) :
            df_buy = pyupbit.get_ohlcv(coin_buy[i])
            #print(df_buy)
            high_buy = df_buy['high']
            #print(high_buy)
            low_buy = df_buy['low']
            close_buy = df_buy['close']
            cci_buy = ta.CCI(high_buy, low_buy, close_buy, timeperiod=20)
            print(coin_buy[i], cci_buy[-1])
            cci_total_today_buy.append(int(cci_buy[-1]))
            cci_total_yesterday_buy.append(int(cci_buy[-2]))
            time.sleep(0.1)

            if cci_total_yesterday_buy[i] <= 50 < cci_total_today_buy[i] :
                print("매수시작")
                my_coin_buy = []
                coin_list = []
                for j in range(len(upbit.get_balances()[0])) :
                    coin_list.append(upbit.get_balances()[0][j])
                    my_coin_buy.append("KRW-" + coin_list[j].get('currency'))
                if my_coin_buy != "KRW-BTC" :
                    if my_coin_buy.count(coin_buy[i]) == 0 :
                        upbit.buy_market_order(coin_buy[i], 5000)
                        print(coin_buy[i] + ":", "매수")
    except Exception as e :
        pass
        print("매수 에러")

    try :
        sell_cur = []
        sell_bal = []
        rsi_total_today_sell = []
        rsi_total_yesterday_sell = []
        cci_total_today_sell = []
        cci_total_yesterday_sell = []
        for x in range(1,len(upbit.get_balances()[0])) :

            df_sell.append(upbit.get_balances()[0][x])
            sell_cur.append("KRW-" + df_sell[x-1].get('currency'))
            sell_bal.append(df_sell[x-1].get('balance'))
            total_sell = sell_cur, sell_bal

            df_coin_sell = pyupbit.get_ohlcv(sell_cur[x-1])
            high_sell = df_coin_sell['high']
            low_sell = df_coin_sell['low']
            close_sell = df_coin_sell['close']

            rsi_sell = ta.RSI(close_sell, timeperiod=14)
            rsi_total_today_sell.append(int(rsi_sell[-1]))
            rsi_total_yesterday_sell.append(int(rsi_sell[-2]))

            cci_sell = ta.CCI(high_sell, low_sell, close_sell, timeperiod=20)
            cci_total_today_sell.append(int(cci_sell[-1]))
            cci_total_yesterday_sell.append(int(cci_sell[-2]))


            if rsi_total_yesterday_sell[x-1] >= 70 > rsi_total_today_sell[x-1] \
                    or cci_total_yesterday_sell[x-1] >= 100 > cci_total_today_sell[x-1] \
                    or cci_total_today_sell[x-1] < 40 :
                upbit.sell_market_order(total_sell[0][x], total_sell[1][x])
                print(sell_cur[x] + ":", "매도완료")


    except Exception as e :
        pass
        print("매도 에러")
    print("END")
    time.sleep(10)















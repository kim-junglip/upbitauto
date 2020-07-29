import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
#print(df.tail(20))
#yesterday = df.iloc[-20:]


def CCI_today_M(ticker):#CCI M값 구하기
    M = (df['high'] + df['low'] + df['close']) /3

    return M[-2]

def CCI_today_m(tiker):
    H = df['high']
    L = df['low']
    C = df['close']
    high = H.rolling(3).mean()
    low = L.rolling(3).mean()
    close = C.rolling(3).mean()
    sum = (high + low + close) / 3

    return sum[-2]


def CCI_d(ticker):#단순 이동편균 20일 구하기

    M = (df['high'] + df['low'] + df['close']) / 3
    H = df['high']
    L = df['low']
    C = df['close']
    high = H.rolling(3).mean()
    low = L.rolling(3).mean()
    close = C.rolling(3).mean()
    sum = (high + low + close) / 3
    total = 0
    for i in range(2,5) :
        d = abs(M[-i]-sum[-i])
        total += d
        d_total = total / 3
    #print(d_total)

    return d_total




def CCI_today_d(ticker):#CCI d 값 구하기
    d = CCI_d("KRW-BTC") / 3

    return d

CCI_1 = (CCI_today_M("KRW-BTC") - CCI_today_m("KRW-BTC"))
CCI_2 = (CCI_today_d("KRW-BTC") * 0.015)
CCI_tot = CCI_1 / CCI_2

#print(CCI_today_M("KRW-BTC"))
#print(CCI_today_m("KRW-BTC"))
#print(CCI_today_d("KRW-BTC"))
#print(CCI_1)
#print(CCI_2)
print(CCI_tot)

#print(CCI_today_M("KRW-BTC"))

#print(CCI_today_M("KRW-BTC"))
#print(CCI_today_m("KRW-BTC"))
#print(CCI_today_d("KRW-BTC"))

#print(abs(d))


#print(CCI_today_M("KRW-BTC"))



#print(get_today_ma20("KRW-BTC"))
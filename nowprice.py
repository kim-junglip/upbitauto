import pyupbit

#price = pyupbit.get_current_price("KRW-XRP")                                                                            #리플의 현재가를 불러온다.
price = pyupbit.get_current_price(["KRW-ALL"])     #여러 코인의 현재가를 불러온다(리스트 형식)
for k, v in all.items():


    print(k, v)
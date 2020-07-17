import pyupbit
import time
import datetime


with open("upbit.txt") as f:
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    upbit = pyupbit.Upbit(key, secret)


upbit = pyupbit.Upbit(key, secret)
print(upbit.get_balances())
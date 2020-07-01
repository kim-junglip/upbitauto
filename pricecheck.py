import pyupbit

access_key =
secret_key =

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())
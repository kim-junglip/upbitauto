import pyupbit

access_key = "HyZz5dIuxdqqJROmHmKJB9aBODOpKtvxD50pXCzZ"
secret_key = "QnGPbfTUUN2HyRLJKdyKLLrQckGKPPN27wfgMn6k"

upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())
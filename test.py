import pyupbit
access = "ysIxUacDVX2ac6O3mrPIfRPilJMFWFwN0AxRT3xZ"
secret = "eilLSad8pyoHnnxrxrCSBnjTHb7aH0x6e8UztTJA"
upbit = pyupbit.Upbit(access, secret)
print(upbit.get_balance("KRW_XRP")) #KRW_XRP 조회
print(upbit.get_balance("KRW-BTC"))     #보유현금조회

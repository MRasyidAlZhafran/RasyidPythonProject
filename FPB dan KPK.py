import math
angkapertama = int(input("Tulis angka pertama: "))
angkakedua = int(input("Tulis angka kedua: "))
fpb = math.gcd(angkapertama, angkakedua)
kpk = (angkapertama * angkakedua) // fpb
print(f"FPB dari {angkapertama} dan {angkakedua} = {fpb}")
print(f"KPK dari {angkapertama} dan {angkakedua} = {kpk}")
bilangan = int(input("Masukkan bilangan: "))

faktorial = 1

if bilangan < 0:
    print("Maaf, faktorial tidak dapat dihitung untuk bilangan negatif")

elif bilangan == 0:
    print("Faktorial dari 0 adalah 1")

else:
    for i in range(1, bilangan + 1):
        faktorial *= i
        print(f"Faktorial dari {bilangan} adalah {faktorial}")
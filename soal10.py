list_tunai = [50000, 300000, 500000, 1000000]
list_atm = ["Tarik Tunai", "Cek Saldo"]
saldo = int(input("Masukkan Saldo Anda \t\t: "))
for i,x in enumerate(list_atm):
    print(f">{i+1} {x}")
pilihan = input("Pilih >1/>2 \t\t: ")
if pilihan == ">1":
    for l,k in enumerate(list_tunai):
        print(f">{l+1} {k}")
    tarik_tunai = input("Pilih >1/>2/... \t\t: ")
    if tarik_tunai == ">1":
        if saldo >= 50000:
            print(f"Total Yang Kamu Tarik Adalah \t: {list_tunai[0]}")
        else:
            print("Saldo Anda Kurang")
    elif tarik_tunai == ">2":
        if saldo >= 300000:
            print(f"Total Yang Kamu Tarik Adalah \t: {list_tunai[1]}")
        else:
            print("Saldo Anda Kurang")
    elif tarik_tunai == ">3":
        if saldo == 500000:
            print(f"Total Yang Kamu Tarik Adalah \t: {list_tunai[2]}")
        else:
            print("Saldo Anda Kurang")
    elif tarik_tunai == ">4":
        if saldo == 1000000:
            print(f"Total Yang Kamu Tarik Adalah \t: {list_tunai[3]}")
        else:
            print("Saldo Anda Kurang")
    else:
        print("Kode Tidak Valid!")

elif pilihan == ">2":
    print(f"Saldo Anda \t\t\t: {saldo}")

else:
    print("Tidak Ada Dalam Pilihan")
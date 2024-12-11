import random
gratis_barang_tablet = ["Casing", "Power Bank", "Tempered Glass", "HeadPhone", "TWS"]
acak_tablet = random.choice(gratis_barang_tablet)
gratis_barang_HP = ["Tempered Glass", "Power Bank", "TWS", "Casing", "Stiker"]
acak_HP = random.choice(gratis_barang_HP)
gratis_barang_laptop = ["Mouse", "Tas", "Mouse Pad"]
acak_laptop = random.choice(gratis_barang_laptop)
list_barang = ["HP", "Laptop", "Tablet"]

for i,x in enumerate(list_barang):
    print(f"{i+1}. {x}")

barang = int(input("Masukkan Nomor Barang \t: "))
if barang == 1:
    print("1000000 - 12000000")
elif barang == 2:
    print("4000000 - 20000000")
elif barang == 3:
    print("3000000 - 12000000")
harga = int(input("Masukkan Harga Nya \t: "))

if barang == 1:
    if harga >= 1000000 and harga <= 12000000:
        if harga >= 5000000:
            print(f"Barangnya \t\t: {list_barang[0]}")
            print(f"Gratis \t\t\t: {acak_HP}")
        else:
            print(f"Barangnya \t\t: {list_barang[0]}")
    else:
        print("Barang Tidak Ada")

if barang == 2:
    if harga >= 4000000 and harga <= 20000000:
        if harga >= 7500000:
            print(f"Barangnya \t\t: {list_barang[1]}")
            print(f"Gratis \t\t\t: {acak_laptop}")
        else:
            print(f"Barangnya \t\t: {list_barang[1]}")
    else:
        print("Barang Tidak Ada")

if barang == 3:
    if harga >= 3000000 and harga <= 12000000:
        if harga >= 6000000:
            print(f"Barangnya \t\t: {list_barang[2]}")
            print(f"Gratis \t\t\t: {acak_tablet}")
        else:
            print(f"Barangnya \t\t: {list_barang[2]}")
    else:
        print("Barang Tidak Ada")

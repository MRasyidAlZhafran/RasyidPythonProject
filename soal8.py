print("Jika Membeli 5 Baju Maka, Akan Diskon 6%. Dan Jika Membeli 7 Celana Maka, Akan Diskon 9%")

nama_barang = input("Masukkan Nama Barang (Baju/Celana) \t: ").strip()
jumlah_barang = int(input("Masukkan Jumlah Barang \t\t\t: "))
nama_barang = nama_barang.lower()

print("Hasilnya Adalah :")
print(f"Nama Barang \t\t\t\t: {nama_barang}")
print(f"Jumlah Barang \t\t\t\t: {jumlah_barang}")

if nama_barang == "baju":
    harga1 = 50000
    total_bayaran1 = jumlah_barang * harga1
    if jumlah_barang >= 5:
        diskon1 = total_bayaran1 * 0.8
        integer = round(diskon1)
        print(f"Total Bayaran \t\t\t\t: {total_bayaran1}")
        print(f"Diskon Menjadi \t\t\t\t: {integer}")
    else:
        print(f"Total Bayaran \t\t\t\t: {total_bayaran1}")
elif nama_barang == "celana":
    harga2 = 40000
    total_bayaran2 = jumlah_barang * harga2
    if jumlah_barang >= 7:
        diskon2 = total_bayaran2 * 0.7
        integer = round(diskon2)
        print("Total Bayaran \t\t\t\t:",total_bayaran2)
        print("Diskon Menjadi \t\t\t\t:",integer)
    else:
        print("Total Bayaran \t\t\t\t:",total_bayaran2)
else:
    print("Mungkin Barang Tersebut Tidak Di Jual Di Sini")
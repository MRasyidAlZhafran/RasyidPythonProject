nama_barang = input("Masukkan Nama Barang \t\t\t\t: ").strip()
jumlah_barang = int(input("Masukkan Jumlah Barang Yang Ingin Di Beli \t: "))
nama_barang = nama_barang.lower()

if nama_barang == "kertas":
    harga_barang = 1000
    if jumlah_barang >= 30:
        ketersediaan = False
    else:
        ketersediaan = True
    
elif nama_barang == "buku":
    harga_barang = 10000
    if jumlah_barang >= 40:
        ketersediaan = False
    else:
        ketersediaan = True
elif nama_barang == "pensil":
    harga_barang = 2000
    if jumlah_barang >= 50:
        ketersediaan = False
    else:
        ketersediaan = True
elif nama_barang == "penghapus":
    harga_barang = 2500
    if jumlah_barang >= 40:
        ketersediaan = False
    else:
        ketersediaan = True

total_harga = jumlah_barang * harga_barang

print(f"Nama Barang \t\t\t\t\t: {nama_barang}")
print(f"Harga Barang \t\t\t\t\t: {harga_barang}")
print(f"Jumlah Barang \t\t\t\t\t: {jumlah_barang}")
print(f"Total Harga \t\t\t\t\t: {total_harga}")
print(f"Ketersediaan \t\t\t\t\t: {ketersediaan}")
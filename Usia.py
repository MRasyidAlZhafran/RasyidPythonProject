print("Menghitung Usia")

usia = int(input("Masukkan Usia : "))

if usia < 6:
    print("Usia Balita")
elif usia < 13:
    print("Usia Masih Anak - Anak")
elif usia < 26:
    print("Usia Sudah Remaja")
elif usia < 35:
    print("Usia Sudah Mulai Tua")
else:
    print("Usia Sudah Tua")
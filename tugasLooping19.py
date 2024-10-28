jumlah = int(input("Masukkan jumlah nilainya \t: "))

total = 0

for a in range(jumlah):
    nilai1 = int(input("Masukkan Nilainya \t\t: "))
    total += nilai1

rata_rata = total / jumlah
print("Jumlah Nilai Adalah \t\t:",total)
print("Rata - Rata Nilainya Adalah \t:",rata_rata)

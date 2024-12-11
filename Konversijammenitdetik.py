print("Konversi Detik ke Jam, Menit, Detik")

detik1 = int(input("Masukkan Detiknya :"))
detik = detik1 % 60
menit = int(detik1 / 60)
jam = int(detik1 / 3600)
print(f"{detik1} Dikonversikan Meenjadi Jam \t: {jam} Jam")
print(f"{detik1} Dikonversikan Menjadi Menit \t: {menit} Menit")
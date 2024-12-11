#Nilai Rapot Siswa

nama = input("Masukkan Nama Siswa\t: ")
nilai = int(input("Masukkan Nilainya\t: "))

if 90 <= nilai < 100:
    tingkat = "A"
elif 75 <= nilai < 90:
    tingkat = "B"
elif 65 <= nilai < 75:
    tingkat = "C"
elif 55 <= nilai < 65:
    tingkat = "D"
else:
    tingkat = "E"

print(f"Nama\t\t\t: {nama}")
print(f"Nilai\t\t\t: {nilai}")
print(f"Peringkat \t\t: {tingkat}")
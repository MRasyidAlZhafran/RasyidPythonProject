Panjang = int(input("Masukan Panjang \t:"))
Lebar = int(input("Masukan Lebar \t\t:"))
Tinggi = int(input("Masukan Tinggi \t\t:"))

luas_balok = 2 * (Panjang * Lebar + Panjang * Tinggi + Lebar * Tinggi)
keliling__balok = 4 * (Panjang + Lebar + Tinggi)

print("Luas Permukaan Balok \t:",luas_balok,"cm3")
print("Keliling Balok \t\t:",keliling__balok,"cm3")
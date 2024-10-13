r = int(input("Masukan Jari - Jari \t:"))
t = int(input("Masukan Tingginya \t:"))
la = int(input("Masukan Luas Alas \t:"))
ka = int(input("Masukan Keliling Alas \t:"))

phi = 22/7

luas = (2 * la) + (ka * t)
volume = 1/3 * (phi * r * r * t)

print(f"Luas Kerucut Adalah \t:{luas}")
print(f"Volume Kerucut Adalah \t:{volume}")
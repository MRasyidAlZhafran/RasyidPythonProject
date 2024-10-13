r = int(input("Masukan Jari - Jari \t:"))
t = int(input("Masukan Tingginya \t:"))
la = int(input("Masukan Luas Alas \t:"))
ls = int(input("Masukan Luas Selimut \t:"))

phi = 22/7

luas = la + ls
volume = 1/3 * (phi * r * r * t)

print(f"Luas Kerucut Adalah \t:{luas}")
print(f"Volume Kerucut Adalah \t:{volume}")
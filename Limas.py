la = int(input("Masukan Luas Alas \t\t:"))
ts = int(input("Masukan Tinggi Sisi \t\t:"))
jlst = int(input("Masukan Jumlah Luas Sisi Tegak :"))

luas = la + jlst
volume = 1/3 * (la * ts)

print(f"Luas Limas Adalah \t:{luas}")
print(f"Volume Limas Adalah \t:{volume}")
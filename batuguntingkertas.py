import random

opsi = ["batu", "gunting", "kertas"]
pilih = input("Pilih Batu/Gunting/Kertas \t: ")

musuh = random.choice(opsi)
print("Pilihan Musuh \t\t\t:",musuh)

if pilih == musuh:
    print("Seri/Draw!")
elif pilih == "batu" and musuh == "gunting" or \
pilih == "kertas" and musuh == "batu" or \
pilih == "gunting" and musuh == "kertas":
    print("Kamu Menang!")
else:
    print("Kamu Kalah!")
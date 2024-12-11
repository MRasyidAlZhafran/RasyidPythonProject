import math

sisi = input("Masukkan Sisinya (a/b/c) \t: ")

sisi = sisi.lower()

if sisi == "a":
    b = float(input("Masukkan Sisi b \t\t: "))
    c = float(input("Masukkan Hipotenusa \t\t: "))
    a = math.sqrt(c**2 - b**2)
    print(f"Jadi Sisi a Adalah \t\t: {a}")
elif sisi == "b":
    a = float(input("Masukkan Sisi a \t\t: "))
    c = float(input("Masukkan Hipotenusa \t\t: "))
    b = math.sqrt(c**2 - a**2)
    print(f"Jadi Sisi b Adalah \t\t: {b}")
    
elif sisi == "c":
    a = float(input("Masukkan Sisi a \t\t: "))
    b = float(input("Masukkab Sisi b \t\t: "))
    c = math.sqrt(a ** 2 + b ** 2)
    print(f"Jadi Hipotenusanya Adalah \t\t: {c}")
else:
    print("Inputan Salah!")
#Energi Kinetik = 1/2 * m * v^2

m = float(input("Masukkan Massanya \t\t: "))
v = float(input("Masukkan Kecepatannya \t\t: "))

ek = 1/2 * m * v**2

if ek >= 1000:
    ek1 = ek / 1000
    print(f"Jadi Energi Kinetiknya Adalah\t: {ek} J")
    print(f"DiKonversikan Menjadi\t\t: {ek1} kJ")
else:
    print(f"Jadi Energi Kinetiknya Adalah\t: {ek} J")
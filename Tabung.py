def tabung():

    r = int(input("Masukan Jari - Jari \t: "))
    t = int(input("Masukan Tingginya \t: "))
    la = int(input("Masukan Luas Alas \t: "))
    ka = int(input("Masukan Keliling Alas \t: "))

    phi = 22/7

    luas = lambda r, t, la, ka, phi: (2 * la) + (ka * t)
    volume = lambda r, t, la, ka, phi: 1/3 * (phi * r * r * t)

    print("Luas Kerucut Adalah \t:",luas(r, t, la, ka, phi))
    print("Volume Kerucut Adalah \t:",volume(r, t, la, ka, phi))

tabung()
tabung()
def bola():

    r = int(input("Masukan Jari Jari\t: "))

    phi = 22/7

    luas = lambda r, phi: 4/3 * (phi * r * r * r)
    volume = lambda r, phi: 4 * phi * r * r

    print("Luas Bola Adalah \t:",luas(r, phi))
    print("Volume Bola Adalah \t:",volume(r, phi))

bola()
bola()
bola()
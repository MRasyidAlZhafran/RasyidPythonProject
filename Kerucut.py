def kerucut():

    r = int(input("Masukan Jari - Jari \t: "))
    t = int(input("Masukan Tingginya \t: "))
    la = int(input("Masukan Luas Alas \t: "))
    ls = int(input("Masukan Luas Selimut \t: "))

    phi = 22/7

    luas = lambda r, t, la, ls, phi : la + ls
    volume = lambda r, t, la, ls, phi : 1/3 * (phi * r * r * t)

    print("Luas Kerucut Adalah \t:",luas(r, t, la, ls, phi))
    print("Volume Kerucut Adalah \t:",volume(r, t, la, ls, phi))

kerucut()
kerucut()
kerucut()
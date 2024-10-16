def kubus():

    r = int(input("Masukan Rusuknya \t: "))

    luas = lambda r : 6 * r * r
    volume = lambda r : r * r * r

    print("Luas Kubus Adalah \t:",luas(r))
    print("Volume Kubus Adalah \t:",volume(r))

kubus()
kubus()
kubus()
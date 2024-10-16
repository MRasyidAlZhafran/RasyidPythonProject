def limas():

    la = int(input("Masukan Luas Alas \t\t: "))
    ts = int(input("Masukan Tinggi Sisi \t\t: "))
    jlst = int(input("Masukan Jumlah Luas Sisi Tegak  : "))

    luas = lambda la, ts, jlst: la + jlst
    volume = lambda la, ts, jlst: 1/3 * (la * ts)

    print("Luas Limas Adalah \t\t:",luas(la, ts, jlst))
    print("Volume Limas Adalah \t\t:",volume(la, ts, jlst))

limas()
limas()
limas()
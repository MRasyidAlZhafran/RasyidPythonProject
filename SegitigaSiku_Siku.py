def segitigasikusiku():
    sa = int(input("Masukkan Sisi a \t: "))
    sb = int(input("Masukkan Sisi b \t: "))
    sc = int(input("Masukkan Sisi c \t: "))
    alas = int(input("Masukkan Alasnya \t: "))
    tinggi = int(input("Masukkan Tingginya \t: "))

    keliling = lambda sa, sb, sc: sa + sb + sc
    luas = lambda alas, tinggi: 1/2 * alas * tinggi

    print("Luas Segitiga SIku - Siku Adalah \t: ",luas(alas, tinggi))
    print("Keliling Segitiga Siku - Siku Adalah \t: ",keliling(sa, sb, sc))

segitigasikusiku()
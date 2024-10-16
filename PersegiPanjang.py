def persegipanjang():

    panjang = int(input("Masukan Nilai Sisi \t: "))
    lebar = int(input("Masukan Nilai Sisi \t: "))

    Luas = lambda panjang, lebar: panjang * lebar
    Keliling = lambda panjang, lebar: 2 * (panjang + lebar)

    print("Luasnya Adalah \t\t:",Luas(panjang, lebar),"cm2")
    print("Kelilingny Adalah \t:",Keliling(panjang, lebar),"cm3")

persegipanjang()
persegipanjang()
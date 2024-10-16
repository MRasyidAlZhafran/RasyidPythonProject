def balok():

    Panjang = int(input("Masukan Panjang \t: "))
    Lebar = int(input("Masukan Lebar \t\t: "))
    Tinggi = int(input("Masukan Tinggi \t\t: "))

    luas_balok = lambda Panjang, Lebar, Tinggi: 2 * (Panjang * Lebar + Panjang * Tinggi + Lebar * Tinggi)
    keliling_balok = lambda Panjang, Lebar, Tinggi: 4 * (Panjang + Lebar + Tinggi)

    print("Luas Permukaan Balok \t:",luas_balok(Panjang, Lebar, Tinggi),"cm3")
    print("Keliling Balok \t\t:",keliling_balok(Panjang, Lebar, Tinggi),"cm3")

balok()
balok()
balok()
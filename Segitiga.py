def segitiga():

    alas = int(input("Masukan Alas \t\t: ")) 
    tinggi = int(input("Masukan Tinggi \t\t: "))
    sisii = int(input("Masukan Sisi \t\t: "))

    luas_segitiga = lambda alas, tinggi, sisii: 1/2 * alas * tinggi
    keliling_segitga = lambda alas, tinggi, sisii: 3 * sisii

    print("Luas Segitiga \t\t:",luas_segitiga(alas, tinggi, sisii),"cm2")
    print("Keliling Segitiga \t:",keliling_segitga(alas, tinggi, sisii),"cm2")

segitiga()
segitiga()
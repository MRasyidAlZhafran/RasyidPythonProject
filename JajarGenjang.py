def jajargenjang():

    a = int(input("Masukan Alasnya \t: "))
    t = int(input("Masukan Tingginya \t: "))
    sa = int(input("Masukan Sisi 1 \t\t: "))
    sb = int(input("Masukan Sisi 2 \t\t: "))

    luas = lambda a, t, sa, sb : a * t
    keliling = lambda a, t, sa, sb : 2 * (sa + sb)

    print("Luasnya Adalah \t\t:",luas(a, t, sa, sb),'cm3')
    print("Kelilingnya Adalah \t:",keliling(a, t, sa, sb),'cm3')

jajargenjang()
jajargenjang()
jajargenjang()
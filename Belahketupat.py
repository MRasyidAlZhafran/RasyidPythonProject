def belahketupat():

    d1 = int(input("Masukkan Nilai Diagonal 1 \t\t:"))
    d2 = int(input("Masukkan Nilai Diagonal 2 \t\t:"))
    s = int(input("Masukkkan NIlai Sisi \t\t\t:"))

    luas = lambda d1, d2: 1/2 * (d1 * d2)
    keliling = lambda s: 4 * s

    print(f"Luas Dari Belah Ketupat Adalah \t\t:{luas(d1, d2)}")
    print(f"Keliling Dari Belah Ketupat Adalah \t:{keliling(s)}")

belahketupat()
belahketupat()
def trapesium():
    
    pssa = int(input("Masukkan Nilai Panjang Sisi Sejajar Atas \t:"))
    pssb = int(input("Masukkan Nilai Panjang Sisi Sejajar Bawah \t:"))
    t = int(input("Masukkan Nilai Tinggi \t\t\t:"))
    ab = int(input("Masukkan Sisi AB \t\t\t\t:"))
    bc = int(input("Masukkan Sisi BC \t\t\t\t:"))
    cd = int(input("Masukkan Sisi CD \t\t\t\t:"))
    ad = int(input("Masukkan Sisi AD \t\t\t\t:"))
    
    keliling = lambda ab, bc, cd, ad: (ab + bc + cd + ad)
    luas = lambda pssa, pssb: 1/2 * (pssa + pssb) * t

    print(f"Hasil Dari Luas Trapesium Yaitu {luas(pssa,pssb)}")
    print(f"Hasil Dari Keliling Trapesium Yaitu {keliling(ab, bc, cd, ad)}")

trapesium()
trapesium()
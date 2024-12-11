angka1 = 87
angka2 = 66
angka3 = 97

angka_pertama = int(input("Masukkan Tebakan Angka Pertama \t: "))
angka_kedua = int(input("Masukkan Tebakan Kedua \t\t: "))
angka_ketiga = int(input("Masukkan Tebakan Angka Ketiga \t: "))

if angka_pertama == angka1:
    print("Jawaban Anda Benar!")
else:
    print("Tebakan Mu Salah!")
    if angka_pertama >= angka1:
        print("Jawaban Terlalu Besar Dari Angka Pertama!")
    else:
        angka_pertama <= angka1
        print("Jawaban Terlalu Kecil Dari Angka Pertama!")
if angka_kedua == angka2:
    print("Tebakan Mu Benar!")
else:
    print("Tebakan Mu Salah!")
    if angka_kedua >= angka2:
        print("Jawaban Terlalu Besar Dari Angka Kedua!")
    else:
        angka_kedua <= angka2
        print("Jawaban Terlalu Kecil Dari Angka Kedua!")
if angka_ketiga == angka3:
    print("Tebakan Mu Benar!")
else:
    print("Tebakan Mu Salah!")
    if angka_ketiga >= angka3:
        print("Jawaban Terlalu Besar Dari Angka Ketiga!")
    else:
        angka_ketiga <= angka3
        print("Jawaban Terlalu Kecil Dari Angka Ketiga!")

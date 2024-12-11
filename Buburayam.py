print('=' * 90)
print('''Buat sebuah program yang menanyakan apakah user menyukai bubur ayam. Jika user menyatakan tidak, cetak ‘Cobain lagi deh kapan-kapan, sehat dan bergizi, siapa tahu jadi suka‘. Jika user menyatakan ya, tanyakan apakah ia suka bubur ayam yang diaduk atau tidak. Jika ia tidak suka bubur ayam yang isinya diaduk, cetak ‘Wow ternyata anda orangnya elegan‘, jika ia menjawab suka bubur ayam yang diaduk, cetak "Yang Penting Enak"  ''')
print('=' * 90)

bubur = input("Apakah Anda Suka Bubur (Iya/Tidak)?\t\t: ")
bubur = bubur.lower()

if bubur == "tidak":
    print("Mungkin lain kali")
elif bubur == "iya":
    aduk = input("Suka Bubur Di Aduk Atau Tidak (Iya/Tidak)?\t: ")
    aduk = aduk.lower()
    if aduk == "tidak":
        print("Wow Kamu Orangnya Elegan")
    elif aduk == "iya":
       print("Yang Pemting Mah Enak :)")
       
    else:
        print("Inputan Tidak Valid!")
else:
    print('Inputan Tidak Valid! Coba Masukkan "iya" atau "tidak"')
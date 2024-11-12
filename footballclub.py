liga = input("Masukkan Liga Sepak Bola (Inggris/Spanyol/Italia): ")
clubinggris = ["Manchester United", "Liverpool", "Arsenal", "Manchester City","Chelsea"]
clubspanyol = ["Real Madrid", "Barcelona", "Atletico Madrid", "Bilbao", "Valencia"]
clubitalia = ["Juventus", "Inter Milan", "AC Milan", "Genoa", "Torino"]
liga = liga.lower()

if liga == "inggris":
    print("Club Inggris :")
    print(clubinggris)
    print("Club Club Ini Pernah Menguasai Liga Tersebut Pada Masanya")
elif liga == "spanyol":
    print("Club Spanyol :")
    print(clubspanyol)
    print("Real Madrid Dan Barcelona Yaitu Pemilik Piala Terbanyak")
elif liga == "italia":
    print("Club Italia :")
    print(clubitalia)
else:
    print("Mungkin Inputan Salah, Coba Pilih: (Inggris/Spanyol/Italia)")
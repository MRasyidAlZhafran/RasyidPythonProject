#mil = kilometer * 0.621371
def kilometer_ke_mil(km):
    kilometer = km * 0.621371
    return kilometer
    
km1 = float(input("Masukkan Kilometernya \t: "))
konversi_kilometer = kilometer_ke_mil(km1)
print(f"Jadi Kilometernya {km1} Di Konversikan Menjadi {konversi_kilometer:.2f}")
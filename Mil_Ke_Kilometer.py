def mil_ke_kilometer(mil):
    km = mil * 1.60934
    return km
mil1 = float(input("Masukkan jarak dalam mil: "))
kilometer = mil_ke_kilometer(mil1)
print(f"{mil1} mil di konversikan menjadi {kilometer:.2f} km")
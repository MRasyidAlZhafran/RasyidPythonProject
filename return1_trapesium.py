def luas(pssa, pssb ,tinggi):
    luas_trapesium = 1/2 * (pssa + pssb) * tinggi
    return luas_trapesium

def keliling(ab, bc, cd, ad):
    keliling_trapesium = ad + bc + cd + ad
    return keliling_trapesium

luas_trapesium = luas(4,5,6)
keliling_trapesium = keliling(3,2,5,4)

print(f"Luas Trapesium Adalah \t\t: {luas_trapesium}")
print(f"Keliling Trapesium Adalah \t: {keliling_trapesium}")
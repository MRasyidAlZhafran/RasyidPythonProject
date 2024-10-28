jumlah = 0
for c in range(2, 11, 2):
    if c < 10:
        print(c, end = " + ")
    else:
        print(c, end = " = ")
    
    jumlah = jumlah + (c)
print(jumlah)
jumlah = 0
for c in range(1,6):
    if c < 5:
        print(c, end = " + ")
    else:
        print(c, end = " = ")

    jumlah = jumlah + (c + 1)
print(jumlah)
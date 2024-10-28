jumlah = 0
for c in range(1,6,2):
    if c < 5:
        print(c, end= " + ")
    else:
        print(c, end= " = ")

    jumlah = jumlah + (c)
print(jumlah)
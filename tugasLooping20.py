x = int(input("Masukkan Nilai Perkalian :"))

print("    *", end = "")
for a in range(1, x + 1):
    print(f"{a:5}", end = "")
print()

for a in range(1, x + 1):
    print(f"{a:5}", end = "")
    for b in range(1, x + 1):
        print(f"{a * b:5}", end = "")
    print()
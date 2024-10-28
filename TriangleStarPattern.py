c = 2 * 5 - 2
for a in range(0, 5):
    for b in range(0, c):
        print(end=" ")
    c = c - 1
    for d in range(0, a + 1):
        print("* ", end="")
    print()
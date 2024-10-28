c = 2 * 5 - 2
for a in range(-1, 4):
    for b in range(0, c):
        print(end=" ")
    c = c - 1
    for d in range(0, a + 1):
        print("* ", end="")
    print()
    
c = 5 - 2
for a in range(4, -1, -1):
    for b in range(c, 0, -1):
        print(end=" ")
    c = c + 1
    for d in range(0, a + 1):
        print("* ", end="")
    print()
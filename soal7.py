print("Memilih Tim")

team = ["Bandung", "Jakarta", "Cianjur"]
kelompok = ["Team 1", "Team 2", "Team 3"]

nama = input("Nama Mu Siapa \t\t\t: ")
for i,x in enumerate(team):
    print(i+1,".",x)
list1 = int(input("Masukkan Nomor Team Anda \t: "))
for a,r in enumerate(kelompok):
    print(a+1,".",r)
list2 = int(input("Masukkan Nomor Kelompok Anda \t: "))

print(f"Nama \t: {nama}")

if list1 == 1:
    print(team[0])
    if list2 == 1:
        print(kelompok[0])
    elif list2 == 2:
        print(kelompok[1])
    elif list2 == 3:
        print(kelompok[2])
    else:
        print("Nomor Tidak Dapat DiKetahui!")
elif list1 == 2:
    print(team[1])
    if list2 == 1:
        print(kelompok[0])
    elif list2 == 2:
        print(kelompok[1])
    elif list2 == 3:
        print(kelompok[2])
    else:
        print("Nomor Tidak Dapat DiKetahui!")
elif list1 == 3:
    print(team[2])
    if list2 == 1:
        print(kelompok[0])
    elif list2 == 2:
        print(kelompok[1])
    elif list2 == 3:
        print(kelompok[2])
    else:
        print("Nomor Tidak Dapat DiKetahui!")
else:
    print("Nomor Tidak Dapat DiKetahui!")
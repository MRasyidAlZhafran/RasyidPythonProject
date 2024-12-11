print("Translate Hari")

list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
english = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i,x in enumerate(list_hari):
    print(i+1,".",x)

hari = int(input("Masukkan Nomor Hari \t: "))

if hari == 1:
    print(list_hari[0])
    print(english[0])
elif hari == 2:
    print(list_hari[1])
    print(english[1])
elif hari == 3:
    print(list_hari[2])
    print(english[2])
elif hari == 4:
    print(list_hari[3])
    print(english[3])
elif hari == 5:
    print(list_hari[4])
    print(english[4])
elif hari == 6:
    print(list_hari[5])
    print(english[5])
elif hari == 7:
    print(list_hari[6])
    print(english[6])
else:
    print("Inputan Hari Terlalu Jauh!")
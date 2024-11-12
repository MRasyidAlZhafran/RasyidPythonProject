#Energi Potensial = m*g*h

print("g = 10 m/s")
m = int(input("Masukkan Massanya \t:"))
h = int(input("Masukkan Tingginya \t:"))

g = 10 

ep = (m * g * h)

if ep >= 1000:
   ep1 = ep / 1000
   print(f"Jadi Hasilnya Adalah {ep1} kJ")
else:
   print(f"Jadi Hasilnya Adalah: {ep} J")
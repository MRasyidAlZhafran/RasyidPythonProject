#Energi Potensial = m*g*h

print("g = 10 m/s")
m = float(input("Masukkan Massanya \t: "))
h = float(input("Masukkan Tingginya \t: "))

g = 10 

ep = (m * g * h)

if ep >= 1000:
   ep1 = ep / 1000
   print(f"Jadi Hasilnya Adalah \t: {ep} J")
   print(f"Dikonversikan Menjadi \t: {ep1} kJ")
else:
   print(f"Jadi Hasilnya Adalah \t: {ep} J")
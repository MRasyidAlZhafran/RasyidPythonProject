#list = [100, 200, 300, 400, 500]
#list = list[::-1]
#print(list)

#list1 = [1, 2, 3, 4, 5, 6]

#res = []

#for i in list1:
    #res.append(i * i)
#print(res)

#z = 0

#while z < 5:
    #if z == 0:
        #print("z is",z)
        #z += 1
    #elif z == 1:
        #print("z is",z)
        #z += 2
    #else:
        #print("z is",z)
        #z += 1

#cities = ["London", "Istanbul", "Houston", "Rome"]
#i = 0
#while i < len(cities):
    #print(cities[i])
    #i += 1

#item = list(input("Masukkan item yang mau di beli : "))

#print(f"Jumlah Item Adalah {len(item)}")

#if item == 1:
    #harga = 15000
#elif item == 2:
    #harga = 30000
#elif item == 3:
    #harga = 45000
#elif item == 4:
    #harga = 60000
#elif item >= 5:
    #harga = item * 15000
#else:
    #print("Item Tidak Valid!")

#def luas_persegi (sisi):
  #return sisi * sisi

#luas_persegi1 = luas_persegi(5)
#print("Luas persegi adalah :",luas_persegi1)

#def hitung_luas_segitiga(alas, tinggi):
  #return (alas * tinggi) / 2
    
#print("Luas segitiga adalah:", hitung_luas_segitiga(5, 7))

#def harga_setelah_pajak(harga_cilok):
  #porsicilok = harga_cilok + (harga_cilok * 10/100)
  #return porsicilok
 

#print("Harga cilok 1 porsi Rp.", harga_setelah_pajak(5000))

#def double_return(n):
    #if(n):
        #return 'Eksekusi return pertama'
    #else:
        #return 'Eksekusi return kedua'
#print(double_return(n=89))

#def multiple_return(n):
    #if(n!=2):
        #return 'Bilangan ganjil'
    #if(n!=3):
        #return 100
    #else:
        #return False
#print(multiple_return(n=8))\

#def tiga_nilai():
    #a = 100
    #b = 200
    #c = 300
    #return a, b, c
#print("Nilainya Adalah : {}, {}, {}.".format(*tiga_nilai()))

#x = int(input("Masukkan Jumlah Perkalian:"))

#for a in range(1, 11):
    #print(f"{x} x {a} = {x * a}")   
#print()

#def persegi(sisi):
    #hasil_persegi = sisi * 4
    #return hasil_persegi

#hasil_perkalian = persegi(4)
#print(f"Jadi Hasilnya Adalah \t: {hasil_perkalian}")
#import math

#def volume(jari_jari, tinggi):
    #volume_tabung = math.pi * jari_jari**2 * tinggi
    #return volume_tabung

#def luas_permukaan(jari_jari, tinggi):
    #luas_tabung = 2 * math.pi * jari_jari**2 * (jari_jari + tinggi)
    #return luas_tabung

#volume_tabung = volume(3,3)
#luas_permukaan_tabung = luas_permukaan(4,4)

#print(f"Luas Permukaan Tabung Adalah \t: {luas_permukaan_tabung}")
#print(f"Volume Tabung Adalah \t\t: {volume_tabung}")

#import calendar

#hc = calendar.HTMLCalendar(calendar.SUNDAY)
#html_str = hc.formatmonth(2025, 1)
#print(html_str)

import tkinter as tk
from tkcalendar import Calendar

root = tk.Tk()
root.title("Kalender")

cal = Calendar(root, selectmode='day', year=2025, month=11, day=24)
cal.pack(pady=20)

root.mainloop()
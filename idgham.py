#print('''Idgham adalah salah satu aspek penting dalam ilmu tajwid Al Quran. 
      #Istilah ini merujuk pada penggabungan atau pengaburan antara dua huruf 
      #yang berbeda dalam bacaan, 
      #yang terjadi dalam beberapa situasi tertentu saat membaca Al Quran.''')

print("Idgham Ada Beberapa Jenis")
print("1. Idgham Bighunnah")
print("2. idgham Bilaghunnah")
print("3. Idgham Mimi")
idgham = int(input("Silahkan Masukkan Jenis Idgham (1/2/3):"))

if idgham == 1:
    print('''
          1. Idgham Bighunnah
          Idgham Bighunnah adalah sebuah aturan dalam tajwid yang berarti 
          menyatukan nun mati atau tanwin dengan huruf yang mengikuti 
          dan membacanya dengan suara yang mendengung. 
          Terdapat empat huruf yang termasuk dalam Idgham Bighunnah, 
          yaitu mim (م), nun (ن), wau (و), dan ya (ي).
          Contohnya:
        "اَبِيْ لَهَبٍ وَّتَبَّ"''')
elif idgham == 2:
    print('''
          2. Idgham Bilaghunnah
          idgham Bilaghunnah yaitu jika nun mati atau tanwin bertemu dengan 
          salah satu huruf Idgham.
          Bilaghunnah, maka dibaca dengan cara menggabungkannya tanpa dengungan.
          Terdapat dua huruf dalam Idgham Bilaghunnah, yaitu lam (ل) dan ra (ر).
          Contohnya:
          "فَوَيْلٌ لِّلْمُصَلِّيْنَ"''')
elif idgham == 3:
    print('''
          3. Idgham Mimi
          Dalam Idgham Mimi, mim mati dileburkan dengan huruf mim berharakat 
          di depannya dan dibacanya dengan dengung selama 3 harakat. Terdapat 
          Idgham Mimi yang berlaku ketika mim mati (مْ) bertemu dengan huruf mim 
          berharakat (مَ – مِ – مُ).
          Contohnya: 
          "أَطْعَمَهُمْ مِنْ"''')
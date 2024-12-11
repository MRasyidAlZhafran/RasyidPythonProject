huruf = input("Masukkan Huruf (alif/ba/ta/tsa):")
huruf = huruf.lower()

if huruf == "alif":
    hijaiyah = "ا"
    print(F"{huruf} Adalah {hijaiyah}")
elif huruf == "ba":
    hijaiyah = "ب"
    print(F"{huruf} Adalah {hijaiyah}")
elif huruf == "ta":
    hijaiyah = "ت"
    print(F"{huruf} Adalah {hijaiyah}")
elif huruf == "tsa":
    hijaiyah = "ث"
    print(F"{huruf} Adalah {hijaiyah}")
else:
    print("Mungkin Huruf Belum Dimasukkan Atau Inputan Salah!")
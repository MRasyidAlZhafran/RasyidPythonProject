kata = input("Masukkan Kata (Spasi untuk Memisahkan) \t: ")

daftar = kata.split()
daftar.sort()

urutan = ' '.join(daftar)

print(f"Urutan Sesuai Abjad \t\t\t: {urutan}")
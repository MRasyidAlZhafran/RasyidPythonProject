import random

kata_sandi = 13
angka_kata = "abcdefghijklmnopqrstuvwxyz123456789"
kata_sandi1 = ""

for a in range(kata_sandi):
    kata_sandi1 = kata_sandi1 + random.choice(angka_kata)

print("Kata Sandi : {}".format(kata_sandi1))

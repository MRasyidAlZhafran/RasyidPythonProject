#Bulan Langka/Bulan Lahir Langka

bulan1 = ["Februari", "Januari", "Mei"]
bulan2 = ["Maret", "April", "Juni", "Juli","November","Desember"]
bulan3 = ["September", "Agustus", "Oktober"]
print("Bulan Langka \t:")
for m,n in enumerate(bulan1):
    print(m+1,'.',n)
print("Bulan Umum \t:")
for i,j in enumerate(bulan2):
    print(i+1,'.',j)
print("Bulan Populer \t:")
for k,l in enumerate(bulan3):
    print(k+1,'.',l)
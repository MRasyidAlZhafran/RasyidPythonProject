def persegi():

    sisi = int(input("Masukan  nilai sisi \t: "))

    luass = lambda sisi: sisi * sisi
    keliling = lambda sisi: 4 * sisi

    print('Luas Persegi\t\t:',luass(sisi),'cm2')
    print('Keliling persegi\t:',keliling(sisi),'cm2')

persegi()
persegi()
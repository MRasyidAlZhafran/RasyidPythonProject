def persegi():
    sisi = int(input('Sisi\t\t: '))
    luas = lambda sisi: sisi * sisi
    keliling = lambda sisi: 4 * sisi

    print('Luas\t\t:',luas(sisi), 'cm2')
    print('Keliling\t:',keliling(sisi), 'cm')

persegi()
persegi()
persegi()
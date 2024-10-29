#print('=' * 40)
#print("KALKULATOR")
#print('=' * 40)

print('Pilih Operasi :')
print('1-Penjumlahan')
print('2-Pengurangan')
print('3-Perkalian')
print('4-Pembagian')

operator = int(input('Pilih Operasi :'))
operand1 = float(input('Masukan Angka Pertama \t:'))
operand2 = float(input('Masukan Angka Kedua\t:'))

if operator == 1:
  print('Hasil dari',operand1,'+',operand2,'=',round(operand1+operand2,2))
elif operator == 2:
  print('Hasil dari',operand1,'-',operand2,'=',round(operand1-operand2,2))
elif operator == 3:
  print('Hasil dari',operand1,'*',operand2,'=',round(operand1*operand2,2))
elif operator == 4:
  print('Hasil dari',operand1,'/',operand2,'=',round(operand1/operand2,2))
elif operator == 5:
  print('Hasil dari',operand1,'%',operand2,'=',round(operand1%operand2,2))
else:
  print('Maaf Operasi Tersebut Tidak Tersedia :)')

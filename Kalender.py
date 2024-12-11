import calendar

angka = int(input("Masukkan Nomor Bulan (1 - 12)\t: "))

kalender = calendar.TextCalendar(calendar.SUNDAY)
waktu = kalender.formatmonth(2025, angka)
print(waktu)


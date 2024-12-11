from datetime import datetime
sekarang = datetime.now()
kalender = sekarang.strftime("%A, %d of %B on %Y, %I:%M:%S %p")
print(kalender)
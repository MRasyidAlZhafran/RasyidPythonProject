kalimat = "Hello World"
vokal = "aeiouAEIOU"
jumlah_vokal = sum(1 for char in kalimat if char in vokal)
print("Kalimat:",kalimat)
print("Jumlah huruf vokal:", jumlah_vokal)
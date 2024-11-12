#Mengkonversikan Celcius Ke Fahrenheit, Reamur, Kelvin

celcius = int(input("Masukkan Suhu Celciusnya\t\t:"))

fahrenheit = (9/5 * celcius) + 32
reamur = (4/5) * celcius
kelvin = celcius + 273

print(f"Celciusnya: {celcius}°C Ke Fahrenheit Menjadi\t: {fahrenheit}°F")
print(f"Celciusnya: {celcius}°C Ke Reamur Menjadi\t: {reamur}°R")
print(f"Celciusnya: {celcius}°C Ke Kelvin Menjadi\t: {kelvin}°K")
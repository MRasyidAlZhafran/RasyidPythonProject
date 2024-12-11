#Mengkonversikan Fahrenheit Ke Celcius, Reamur, Kelvin

fahrenheit = int(input("Masukkan Suhu Fahrenheitnya\t\t: "))

celcius = 5/9 * (fahrenheit - 32)
reamur = 4/9 * (fahrenheit - 32)
kelvin = 5/9 * (fahrenheit + 459.67) 

print(f"Fahrenheitnya: {fahrenheit}°F Ke Celcius Menjadi\t: {celcius}°C")
print(f"Fahrenheitnya: {fahrenheit}°F Ke Reamur Menjadi\t: {reamur}°R")
print(f"Fahrenheitnya: {fahrenheit}°F Ke Kelvin Menjadi\t: {kelvin}°K")
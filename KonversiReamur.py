#Mengkonversikan Reamur ke Celcius, Fahrenheit, Kelvin

reamur = int(input("Masukkan Suhu Reamurnya \t\t: "))

celcius = (5/4) * reamur
fahrenheit = (9/4 * reamur) + 32
kelvin = (5/4 * reamur) + 273

print(f"Reamurnya : {reamur}°R Ke Celcius Menjadi \t: {celcius}°C")
print(f"Reamurnya : {reamur}°R Ke Fahrenheit Menjadi \t: {fahrenheit}°F")
print(f"Reamurnya : {reamur}°R Ke Kelvin Menjadi \t: {kelvin}°K")
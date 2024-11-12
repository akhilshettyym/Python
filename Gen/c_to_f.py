# Program to convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")
# Program to convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C.")
# Program to convert Celsius to Kelvin
celsius = float(input("Enter temperature in Celsius: "))
kelvin = celsius + 273.15
print(f"{celsius}°C is equal to {kelvin}K.")

# 2. Write a python program using function to convert Celsius to Fahrenheit.
# c/5 = f-32/9
f = int(input("Enter temperature in Celsius :"))
def Fahrenheit(f):
    c = (f - 32) * 5/9
    return c
print(f"Temperature in Fahrenheit is {Fahrenheit(f)}°")

# Write a python program using function to convert Fahrenheit to Celsius.
c = int(input("Enter the temperature in Fahrenheit :"))
def Celsius(c):
    f = (9/5 * c) + 32
    return f
print(f"Temperature in Celsius is {Celsius(c)}°")


# °C = (°F - 32) × 5/9
# °F = (9/5 × °C) + 32.
from converter import celsius_to_fahrenheit

print("Temperature COnverter")

try:
    celsius = float(input("Enter a temperature in celsius: "))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"{celsius}°C is equal to {fahrenheit}°F")

except ValueError:
    print("Invalid input. Please enter a number.")
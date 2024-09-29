# A temperature conversion tool
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9


def convert_to_celsius(fahrenheit):
    """A function to convert temperature from fahrenheit to celsius"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    try:
        CELSIUS = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except:
        return "Invalid temperature. Please enter a numeric value."
    return f"{fahrenheit}°F is {CELSIUS}°C"


def convert_to_fahrenheit(celsius):
    """A function to convert temperature from celsius to fahrenheit"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    try:
        FAHRENHEIT = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    except:
        return "Invalid temperature. Please enter a numeric value."
    return f"{celsius}°C is {FAHRENHEIT}°F"


temp = int(input("Enter the temperature to convert: "))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
if choice == "C":
    temp = celsius
    convert_to_fahrenheit(celsius)
elif choice == "F":
    temp = fahrenheit
    convert_to_celsius(fahrenheit)
else:
    print("Please enter a choose between C or F")

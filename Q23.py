#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Taking input from the user
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

if unit.upper() == 'C':
    # Convert Celsius to Fahrenheit
    converted_temp = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C is equal to {converted_temp}°F")
elif unit.upper() == 'F':
    # Convert Fahrenheit to Celsius
    converted_temp = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F is equal to {converted_temp}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

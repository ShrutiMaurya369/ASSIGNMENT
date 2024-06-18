#Write a python program that calculates the sum of the digits of a given  number.

# Function to calculate the sum of digits in a number
def sum_of_digits(number):
    # Convert the number to a string to iterate over its digits
    number_str = str(number)

    # Initialize the sum
    digit_sum = 0

    # Iterate over each digit in the number and add it to the sum
    for digit in number_str:
        digit_sum += int(digit)

    return digit_sum


# Taking input from the user
number = int(input("Enter a number: "))

# Calculating and printing the sum of digits
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")


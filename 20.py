# Write a python program that takes a list of numbers and returns their sum.

# Function to calculate the sum of numbers in a list
def calculate_sum(numbers_list):
    total = sum(numbers_list)
    return total

# Taking input from the user
numbers_str = input("Enter a list of numbers separated by spaces: ")

# Splitting the input string into a list of numbers
numbers_list = [float(num) for num in numbers_str.split()]

# Calling the function to calculate the sum
result_sum = calculate_sum(numbers_list)

# Printing the sum
print("Sum of the numbers:", result_sum)

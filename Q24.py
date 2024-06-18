# Write a program that acts as a simple calculator. It should take two  numbers and an operator (+, -, *, /) as input and print the result.

# Function to perform arithmetic operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Calling the function to perform the calculation
result = calculate(num1, num2, operator)

# Printing the result
print(f"Result: {result}")



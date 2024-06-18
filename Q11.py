#Write a python program that generates the first n numbers in the Fibonacci sequence.

# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers

    # Generate the remaining Fibonacci numbers
    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers


# Get input from the user for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the function and print the generated Fibonacci numbers
fibonacci_sequence = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {fibonacci_sequence}")

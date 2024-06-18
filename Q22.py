#Write a python program that returns the minimum and maximum values in a list of numbers.

# Function to find minimum and maximum values in a list
def find_min_max(numbers_list):
    if not numbers_list:  # Check if the list is empty
        return None, None

    # Using built-in functions min() and max() to find minimum and maximum values
    min_value = min(numbers_list)
    max_value = max(numbers_list)

    return min_value, max_value


# Taking input from the user
numbers_str = input("Enter a list of numbers separated by spaces: ")

# Splitting the input string into a list of numbers
numbers_list = [float(num) for num in numbers_str.split()]

# Calling the function to find minimum and maximum values
min_val, max_val = find_min_max(numbers_list)

# Printing the minimum and maximum values
if min_val is not None and max_val is not None:
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")
else:
    print("The list is empty.")

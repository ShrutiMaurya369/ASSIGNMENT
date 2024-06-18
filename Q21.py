#Write a python program that counts the occurrences of a specific element in a list.

# Function to count occurrences of an element in a list
def count_occurrences(input_list, element):
    count = input_list.count(element)
    return count

# Taking input from the user for the list and element
input_list_str = input("Enter a list of elements separated by spaces: ")
element_to_count = input("Enter the element to count: ")

# Splitting the input string into a list of elements
input_list = input_list_str.split()

# Calling the function to count occurrences
occurrence_count = count_occurrences(input_list, element_to_count)

# Printing the count of occurrences
print(f"The element '{element_to_count}' occurs {occurrence_count} time(s) in the list.")

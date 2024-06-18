# Write a program in python that converts a given string to title case (first letter of each word capitalized).

# Function to convert a string to title case
def convert_to_title_case(input_string):
    # Using the title() method to convert the string to title case
    title_case_string = input_string.title()
    return title_case_string

# Taking input from the user
input_string = input("Enter a string: ")

# Calling the function to convert to title case
title_case_result = convert_to_title_case(input_string)

# Printing the title case result
print("String in title case:")
print(title_case_result)

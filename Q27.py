#Write a program in python that converts a string into a list of its characters.


# Function to convert a string to a list of characters
def string_to_list(input_string):
    char_list = list(input_string)
    return char_list

# Taking input from the user
input_string = input("Enter a string: ")

# Calling the function to convert the string to a list of characters
char_list = string_to_list(input_string)

# Printing the list of characters
print("List of characters:")
print(char_list)

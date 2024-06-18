#Write a python program that removes all punctuation from a given string.


import string


# Function to remove punctuation from a string
def remove_punctuation(input_string):
    # Define punctuation characters
    punctuation_chars = string.punctuation

    # Remove punctuation using translate() method
    cleaned_string = input_string.translate(str.maketrans('', '', punctuation_chars))

    return cleaned_string


# Taking input from the user
input_string = input("Enter a string with punctuation: ")

# Calling the function to remove punctuation
cleaned_string = remove_punctuation(input_string)

# Printing the cleaned string
print("String after removing punctuation:")
print(cleaned_string)

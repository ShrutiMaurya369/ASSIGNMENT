#Write a program in python that counts the frequency of each character in a string.

# Function to count the frequency of each character in a string
def count_characters(string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Count the frequency of each character in the string
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency


# Taking input from the user
input_string = input("Enter a string: ")

# Calling the function to count character frequencies
frequency_dict = count_characters(input_string)

# Printing the character frequencies
print("Character frequencies:")
for char, frequency in frequency_dict.items():
    print(f"'{char}': {frequency}")

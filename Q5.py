# Write a program that takes a string input from the user and writes it to a text file.

# Function to write user input to a text file
def write_to_file():
    # Taking input from the user
    user_input = input("Enter a string: ")

    # Writing the input to a text file
    with open("output.txt", "w") as file:
        file.write(user_input)

    print("The input has been written to output.txt")


# Calling the function
write_to_file()

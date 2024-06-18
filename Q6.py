#Write a program that reads the content of a text file and prints it to the console.

# Function to read from a text file and print its content
def read_from_file():
    # File name
    file_name = "output.txt"

    try:
        # Reading the content of the file
        with open(file_name, "r") as file:
            content = file.read()

        # Printing the content to the console
        print("The content of the file is:")
        print(content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")


# Calling the function
read_from_file()

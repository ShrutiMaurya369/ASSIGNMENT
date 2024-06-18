#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.


# Function to read and print multiple lines of input
def read_multiple_lines():
    lines = []  # List to store the lines

    print("Enter multiple lines of input. Press Enter on an empty line to stop.")

    # Reading input until an empty line is entered
    while True:
        line = input()  # Read a line of input
        if line == '':  # Check if the line is empty
            break  # Exit the loop if an empty line is entered
        lines.append(line)  # Add the line to the list

    # Printing all the lines entered
    print("\nLines entered:")
    for line in lines:
        print(line)


# Calling the function
read_multiple_lines()

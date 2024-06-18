#Write a program that asks the user for their birth year and calculates their age.


from datetime import datetime

# Function to calculate age based on birth year
def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Taking input from the user
birth_year = int(input("Enter your birth year: "))

# Calculating and printing the age
age = calculate_age(birth_year)
print(f"You are {age} years old.")


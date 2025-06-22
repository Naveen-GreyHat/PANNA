# Age Calculator Program

def calculate_age():
    # Get user input
    current_year = int(input("Enter the current year: "))
    birth_year = int(input("Enter your birth year: "))

    # Calculate age
    age = current_year - birth_year

    print(f"You are {age} years old.")

calculate_age()

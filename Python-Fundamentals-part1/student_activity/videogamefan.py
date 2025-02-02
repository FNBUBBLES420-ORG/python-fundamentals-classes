# EXAMPLES NOT FOR USE
# --------------------

import os
import time

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

print("Hello coding community!")
time.sleep(1)

language = "Python" # String
dreamjobtitle = "videogame development"
print(f"{language} is my favorite language for programming. My favorite dream job that I want to get is {dreamjobtitle}.")
time.sleep(1)

age = 20  # Define the age variable with a sample value

if age < 18:
    print("Student")
else:
    if age >= 18 and age <= 25:
        print("Junior Developer")
    else:
        print("Senior Developer")
time.sleep(1)

def calculate_income(monthly_salary):
    mid_income = monthly_salary * 6
    return mid_income

# Example usage
monthly_salary = 1000
mid_income = calculate_income(monthly_salary)
print(f"The mid income for 6 months is ${mid_income}")


# STUDENT PASSED ACTIVITY

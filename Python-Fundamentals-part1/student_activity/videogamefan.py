# EXAMPLES NOT FOR USE
# --------------------

import time

# Parameterize the sleep duration
SLEEP_DURATION = 1

def clear_console():
    # Clear the console (optional, can be omitted if not necessary)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

print("Hello coding community!")
time.sleep(SLEEP_DURATION)

language = "Python" # String
dreamjobtitle = "videogame development"
print(f"{language} is my favorite language for programming. My favorite dream job that I want to get is {dreamjobtitle}.")
time.sleep(SLEEP_DURATION)

age = 20  # Define the age variable with a sample value

if age < 18:
    print("Student")
elif 18 <= age <= 25:
    print("Junior Developer")
else:
    print("Senior Developer")
time.sleep(SLEEP_DURATION)

def calculate_six_month_income(monthly_salary):
    """
    Calculate income for a six-month period based on the monthly salary.
    
    Args:
    monthly_salary (float): Monthly salary amount.
    
    Returns:
    float: Total income for six months.
    """
    six_month_income = monthly_salary * 6
    return six_month_income

# Example usage
monthly_salary = 1000
six_month_income = calculate_six_month_income(monthly_salary)
print(f"The income for 6 months is ${six_month_income:.2f}")


# STUDENT PASSED ACTIVITY

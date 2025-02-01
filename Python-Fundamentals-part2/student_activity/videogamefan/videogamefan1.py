# EXAMPLES NOT FOR USE
# --------------------

def divide_numbers():
    try:
        # Taking input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Attempting to divide the numbers
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
    
    except ValueError:
        # Handle invalid input (non-numeric input)
        print("Invalid input! Please enter valid numbers.")
    # continues on next text
    except ZeroDivisionError:
        # Handle division by zero
        print("Error! Division by zero is not allowed.")

# Call the function to run the program
divide_numbers()

# STUDENT PASSED ACTIVITY

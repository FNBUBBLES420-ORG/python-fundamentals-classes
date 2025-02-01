# "Errors can crash programs, but Python’s try-except blocks help handle them gracefully."

# Basic Error Handling:

# Example Code:

try:   # Try block        
    number = int(input("Enter a number: "))  # This line may raise a ValueError if input is not a number
    print(10 / number)  # This line may raise a ZeroDivisionError if number is zero
except ZeroDivisionError:                       
    print("You cannot divide by zero!")  # This block handles division by zero errors
except ValueError:
    print("Please enter a valid number!")  # This block handles invalid input errors (non-integer input)
finally:            
    print("Program finished.")  # This block always executes, regardless of whether an exception was raised or not



# Student Activity:

# Write a program that divides two numbers and handles invalid inputs or division by zero.
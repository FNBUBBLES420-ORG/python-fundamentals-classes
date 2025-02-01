# "Loops are powerful for repeating tasks, but they can do much more when combined with 
# advanced techniques like nested loops and list comprehensions."

# Nested Loops

"A loop inside another loop lets you work with grids or combinations."


# Example Code:
for row in range(3):  # Outer loop iterates over rows
    for col in range(3):  # Inner loop iterates over columns
        print(f"({row}, {col})", end=" ")  # Print the current row and column, stay on the same line
    print()  # Print a newline after each row

# Output:

# Output of the nested loop:
(0, 0) (0, 1) (0, 2)  # First row: columns 0, 1, 2
(1, 0) (1, 1) (1, 2)  # Second row: columns 0, 1, 2
(2, 0) (2, 1) (2, 2)  # Third row: columns 0, 1, 2



# List Comprehensions

"A shorthand way to create lists."



# Example Code:

squares = [x**2 for x in range(5)]  # List comprehension to create a list of squares of numbers from 0 to 4
print(squares)  # Print the list of squares

# Output:

[0, 1, 4, 9, 16]

# 🛠️ Student Activity:
# Create a nested loop to print a 5x5 grid of numbers.
# Use a list comprehension to create a list of even numbers from 0 to 20.



for row in range(3):  # Outer loop iterates over rows
    for col in range(3):  # Inner loop iterates over columns
        print(f"({row}, {col})", end=" ")  # Print the current row and column, stay on the same line
    print()  # Print a newline after each row

squares = [x**2 for x in range(5)]  # List comprehension to create a list of squares of numbers from 0 to 4
print(squares)  # Print the list of squares

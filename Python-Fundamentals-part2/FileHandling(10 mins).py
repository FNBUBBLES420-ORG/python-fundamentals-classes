# "Python allows you to read, write, and update files easily. 
# This is useful for saving data or working with external files."

# Key Methods:

# 1. open(file, mode): Opens a file and returns a file object.

# 'r': Read
# 'w': Write (overwrites existing content)
# 'a': Append
# read() and write() - Read or write data.
# Always close the file with close() or use with.

# Example Code – Writing to a File:

with open("example.txt", "w") as file:  # Open the file "example.txt" in write mode
    file.write("Hello, World!\n")  # Write "Hello, World!" followed by a newline to the file
    file.write("Python is fun!")  # Write "Python is fun!" to the file

# Example Code – Reading from a File:

with open("example.txt", "r") as file:  # Open the file "example.txt" in read mode
    content = file.read()  # Read the entire content of the file
    print(content)  # Print the content of the file

# Output:

print("Hello, World!")  # Print "Hello, World!" to the console
print("Python is fun!")  # Print "Python is fun!" to the console

#  Student Activity:

# Write a program that asks the user for their name and saves it to a file.
# Read the file and display the saved name.


with open("example.txt", "w") as file:  # Open the file "example.txt" in write mode
    file.write("Hello, World!\n")  # Write "Hello, World!" followed by a newline to the file
    file.write("Python is fun!")  # Write "Python is fun!" to the file

with open("example.txt", "r") as file:  # Open the file "example.txt" in read mode
    content = file.read()  # Read the entire content of the file
    print(content)  # Print the content of the file

print("Hello, World!")  # Print "Hello, World!" to the console
print("Python is fun!")  # Print "Python is fun!" to the console
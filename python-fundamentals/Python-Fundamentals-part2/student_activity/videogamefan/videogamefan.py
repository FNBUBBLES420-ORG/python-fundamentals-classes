# Get user input
name = input("What is your name: ")

# Save to file
with open("name.txt", "w") as file:
    file.write(name)

# Read from file
with open("name.txt", "r") as file:
    saved_name = file.read()

# Display saved name
print("Your saved name is:", saved_name)


# PASS
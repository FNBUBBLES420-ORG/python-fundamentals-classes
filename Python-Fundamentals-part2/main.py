# EXAMPLES NOT FOR USE
# --------------------

for row in range(3):  # Outer loop iterates over rows
    for col in range(3):  # Inner loop iterates over columns
        print(f"({row}, {col})", end=" ")  # Print the current row and column, stay on the same line
    print()  # Print a newline after each row

squares = [x**2 for x in range(5)]  # List comprehension to create a list of squares of numbers from 0 to 4
print(squares)  # Print the list of squares

#--------------------------------------------

# Define a class called Car. The Car class should have the following attributes:
# brand (string)
# model (string)
# The Car class should have the following method:
# drive() - This method should print "{brand} says drive!" where {brand} is the brand of the car.
# Create an instance of the Car class and call the drive() method.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} says drive!")

my_car = Car("Toyota", "Corolla")
my_car.drive()  # Output: Toyota says drive!

# Output: Toyota says drive!
# The Car class has two attributes, brand and model, and a method, drive().
# The __init__() method initializes the brand and model attributes.
# The drive() method prints the brand of the car followed by "says drive!".
# The object my_car is an instance of the Car class.
# The drive() method is called on the my_car object, which prints "Toyota says drive!".

# EXAMPLES NOT FOR USE
# --------------------

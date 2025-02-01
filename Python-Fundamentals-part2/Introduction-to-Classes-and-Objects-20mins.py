# "Python is an object-oriented programming language. 
# Classes are blueprints for creating objects, which are instances of these classes."

# Basic Class Example:

class Dog:     # Defines the class.
    def __init__(self, name, age):  # A special method to initialize the object’s attributes.
        self.name = name        # Initializes the name attribute.
        self.age = age      # Initializes the age attribute.

    def bark(self):   # Defines a method.  
        print(f"{self.name} says woof!") # Prints the dog's name and the sound it makes.                                                                                                                        

my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog.bark()       # Output: Buddy says woof!


# Explain Step-by-Step:

# class Dog: Defines the class.

# __init__: A special method to initialize the object’s attributes.

# self: Refers to the current object.

# Methods like bark() define actions the object can perform.

# Student Activity:

# Create a class 'Car' with attributes brand and 'model', and a method 'drive()' that prints "The car is driving."

# Create an object of the 'Car' class and call its methods.

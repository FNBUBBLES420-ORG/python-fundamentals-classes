# Define the Car class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    # Method to simulate driving
    def drive(self):
        print("The car is driving.")
    
    # Optional: Method to display car details
    def display_info(self):
        print(f"Car brand: {self.brand}, Model: {self.model}")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla")

# Call the methods of the Car class
#continues on next text
my_car.display_info()  # Display the car details
my_car.drive()         # Call the drive method

# PASS
# Python Version: Object properties (attributes) have been part of Python's object model since version 1.0.

# Object Properties in Python
# Properties (also known as attributes) are variables that belong to an object.


class Car:
    def __init__(self, make, model, year):
        self.make = make  # Public attribute
        self.model = model
        self.year = year


# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing properties
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
# Outputs: My car is a 2020 Toyota Corolla.

# Modifying properties
my_car.year = 2021
print(f"My car is now a {my_car.year} {my_car.make} {my_car.model}.")
# Outputs: My car is now a 2021 Toyota Corolla.

# Note: Object properties are similar to variables, but they are tied to specific instances of objects.
# Properties can be accessed and modified directly, providing flexibility in how objects store and manage data.

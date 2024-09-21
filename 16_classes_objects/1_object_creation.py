# Python Version: Python has supported object-oriented programming since version 1.0 (January 1994).

# Object Creation in Python
# In Python, objects are instances of classes, which act as blueprints for creating objects.


# Defining a simple class
class Dog:
    # The __init__ method is a special method used to initialize new objects
    def __init__(self, name, age):
        self.name = name  # Assigning properties to the object
        self.age = age


# Creating an object (instance) of the Dog class
my_dog = Dog("Buddy", 5)

# Accessing object properties
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
# Outputs: My dog's name is Buddy and he is 5 years old.

# Note: In Python, everything is an object, including functions and primitive data types.
# Creating objects from classes is a fundamental concept in Python's object-oriented programming.

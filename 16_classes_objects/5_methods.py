# Python Version: Methods have been an integral part of Python's object-oriented model since version 1.0.

# Defining Various Methods in Python
# Methods in Python can be categorized into instance methods, class methods, and static methods.


class MathOperations:
    # Instance method: Operates on an instance of the class
    def add(self, x, y):
        return x + y

    # Class method: Operates on the class itself, not instances
    @classmethod
    def multiply(cls, x, y):
        return x * y

    # Static method: Neither modifies the instance nor the class
    @staticmethod
    def subtract(x, y):
        return x - y


# Creating an instance of the MathOperations class
math_op = MathOperations()

# Calling instance method
print(f"Addition: {math_op.add(5, 3)}")  # Outputs: Addition: 8

# Calling class method
print(f"Multiplication: {MathOperations.multiply(5, 3)}")  # Outputs: Multiplication: 15

# Calling static method
print(f"Subtraction: {MathOperations.subtract(5, 3)}")  # Outputs: Subtraction: 2

# Note: Instance methods are used to operate on object properties.
# Class methods operate on the class itself and are marked with @classmethod.
# Static methods do not modify object state or class state and are marked with @staticmethod.

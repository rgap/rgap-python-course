# Python Version: Function definitions in Python must occur before they are called.

# Function Declaration Order in Python
# Python requires that functions be defined before they are called.


def greet():
    print("Hello, World!")


greet()  # Outputs: Hello, World!

# Attempting to call a function before it is defined will result in an error
# print(greet_before())  # Uncommenting this line will raise NameError: name 'greet_before' is not defined


def greet_before():
    return "Hello before definition!"


# After defining the function, it can be called
print(greet_before())  # Outputs: Hello before definition!

# Note: In Python, function definitions must appear in the code before any calls to the function.
# This is because Python executes code line by line, and a function must be defined before it can be invoked.

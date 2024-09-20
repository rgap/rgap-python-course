# Python Version: Functions have been a fundamental part of Python since
# version 1.0 (January 1994).

# Basic Function in Python
# Functions are reusable blocks of code designed to perform a specific task.
# They help in organizing code, making it more modular, maintainable, and
# reusable.


# Defining a basic function
def greet():
    # This function simply prints a greeting message.
    print("Hello, World!")


# Calling the function
greet()  # Outputs: Hello, World!


##########################################################


# Functions with Parameters
# Parameters allow you to pass data to a function
def greet_user(name):
    # The parameter 'name' is used to customize the greeting.
    print(f"Hello, {name}!")


greet_user("Alice")  # Outputs: Hello, Alice!


##########################################################


# Functions with Return Values
# Functions can return a value using the 'return' statement.
def add(a, b):
    # This function returns the sum of two numbers.
    return a + b


result = add(5, 3)
print(f"Sum: {result}")  # Outputs: Sum: 8


##########################################################


# Default Parameter Values
# Functions can have default parameter values, which are used if no
# argument is provided.
def greet_user_default(name="Guest"):
    # If no name is provided, 'Guest' will be used as the default value.
    print(f"Hello, {name}!")


greet_user_default()  # Outputs: Hello, Guest!
greet_user_default("Bob")  # Outputs: Hello, Bob!


##########################################################


# Positional Arguments and Default Parameter
# When using both positional arguments and default parameters, the default
# parameters must be placed after the positional arguments.
def greet_user(a, b, name="Guest"):
    print(f"Hello, {name}!")
    print(f"Sum: {a + b}")


# Call the function
greet_user(2, 3)  # Outputs: Hello, Guest! Sum: 5
greet_user(2, 3, "Alice")  # Outputs: Hello, Alice! Sum: 5

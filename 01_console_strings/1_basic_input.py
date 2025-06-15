# Python Version: input() function was introduced in Python 2.0 (October 2000)

# The input() function allows you to take input from the user via the console.
# The function pauses the program's execution until the user provides input and presses Enter.

# Using input() to capture a user's name.
name = input(
    "Enter your name: "
)  # The user's input is captured and stored in the variable 'name'.

# The f-string (FORMATTED STRING LITERAL) is a modern way to format strings in Python.
# It allows you to embed expressions inside string literals, using curly braces {}.
print(f"Hello, {name}!")  # Outputs: Hello, <name>!

# Capturing additional input from the user.
# Here, we prompt the user to enter their age.
# Note: input() returns the value as a string, so if you need a numeric type, you must convert it.
age = input("Enter your age: ")

# The f-string is used again to include the value of 'age' in the output string.
print(f"You are {age} years old.")  # Outputs: You are <age> years old.

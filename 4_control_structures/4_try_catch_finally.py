# Try-Except-Finally in Python (Exception Handling)
# Python Version: The try-except-finally structure has been part of Python since version 1.0 (January 1994).

# The try-except-finally structure is used for exception handling in Python, allowing you to manage errors and ensure that cleanup code runs.

# Example: Handling exceptions with try-except-finally
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Outputs: Error: division by zero
finally:
    print(
        "This will always execute, regardless of an error"
    )  # Outputs: This will always execute, regardless of an error

# Catching multiple exceptions
# You can handle different types of exceptions using a tuple in the except clause.
try:
    result = int("abc")  # This will raise a ValueError
except (ValueError, TypeError) as e:
    print(
        f"Error: {e}"
    )  # Outputs: Error: invalid literal for int() with base 10: 'abc'

# Using else with try-except
# The else block executes if no exception was raised in the try block.
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero error")
else:
    print(f"Result: {result}")  # Outputs: Result: 5.0

# Using finally to ensure cleanup
# The finally block is used to release resources or perform cleanup actions.
try:
    file = open("example.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Ensure the file is closed regardless of whether an error occurred
    print("File closed")  # Outputs: File closed

# Note: The try-except-finally structure is essential for writing robust Python code, ensuring that resources are managed and errors are handled gracefully.

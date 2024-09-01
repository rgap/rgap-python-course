# Type Coercion in Python
# Python Version: Type coercion has been a feature of Python since its early versions.

# Type coercion refers to the automatic conversion of one data type to another.

# Implicit type coercion during arithmetic operations
result = (
    10 + 3.5
)  # Here, the integer 10 is implicitly converted to a float before addition
print(
    f"Result: {result} (type: {type(result)})"
)  # Outputs: Result: 13.5 (type: <class 'float'>)

# Explicit type conversion
# Sometimes, you'll need to manually convert types using functions like int(), float(), and str().
num_str = "100"
num_int = int(num_str)  # Explicitly converting string to integer
print(
    f"Converted integer: {num_int} (type: {type(num_int)})"
)  # Outputs: Converted integer: 100 (type: <class 'int'>)

# Note: Python's flexible type system allows for both implicit and explicit type conversions, facilitating dynamic programming.

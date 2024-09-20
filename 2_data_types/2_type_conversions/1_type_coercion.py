# Implicit Type Conversion in Python (Type Coercion)
# Python Version: Implicit type conversion has been a feature of Python since its inception, enabling seamless data type conversions.

# Implicit type conversion (type coercion) refers to the automatic conversion of one data type to another during an operation.
# In Python, this concept is prevalent in many operations.

# Integer to float conversion (implicit)
num = 10
result = num / 2  # The integer 10 is implicitly converted to a float during division
print(f"Result of division: {result} (type: {type(result)})")
# Outputs: 5.0 (type: <class 'float'>)

# Explicit conversion example
age = 30
age_str = "My age is " + str(age)  # The integer 30 is explicitly converted to a string
print(age_str)  # Outputs: My age is 30

# Integer to boolean conversion (implicit)
count = 0
if count:  # The integer 0 is implicitly converted to a boolean (False)
    print("Count is non-zero.")
else:
    print("Count is zero.")  # Outputs: Count is zero.

# Boolean to integer conversion (implicit)
is_valid = True
number = is_valid + 1  # The boolean True is implicitly converted to 1
print(f"Number: {number} (type: {type(number)})")
# Outputs: Number: 2 (type: <class 'int'>)

# Integer to complex conversion (implicit)
real_part = 3
complex_num = (
    real_part + 4j
)  # The integer 3 is implicitly converted to a complex number
print(f"Complex Number: {complex_num} (type: {type(complex_num)})")
# Outputs: Complex Number: (3+4j) (type: <class 'complex'>)

# Note: Python performs implicit type conversions (type coercion) where appropriate,
# but explicit conversion using functions like str(), int(), and float() is often necessary.

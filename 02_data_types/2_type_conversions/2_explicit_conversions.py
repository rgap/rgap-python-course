# Explicit Type Conversion in Python

# Explicit type conversion refers to the deliberate conversion of one data type to another, typically using built-in functions like int(), str(), float(), etc.
# Unlike autoboxing, which is implicit, explicit conversions require the developer to specify the desired type.

# Integer to string conversion (explicit)
age = 30
age_str = str(age)  # Explicit conversion of integer to string
print(age_str)  # Outputs: "30" (type: <class 'str'>)

# Float to integer conversion (explicit)
value = 9.99
int_value = int(value)  # Explicit conversion from float to integer
print(
    f"Integer Value: {int_value} (type: {type(int_value)})"
)  # Outputs: Integer Value: 9 (type: <class 'int'>)

# String to integer conversion (explicit)
num_str = "100"
num_int = int(num_str)  # Explicit conversion of string to integer
print(
    f"Integer Value: {num_int} (type: {type(num_int)})"
)  # Outputs: Integer Value: 100 (type: <class 'int'>)

# Float to string conversion (explicit)
pi = 3.14159
pi_str = str(pi)  # Explicit conversion of float to string
print(
    f"String Value: {pi_str} (type: {type(pi_str)})"
)  # Outputs: String Value: "3.14159" (type: <class 'str'>)

# Boolean to integer conversion (explicit)
is_valid = True
num = int(is_valid)  # Explicit conversion of boolean to integer
print(
    f"Integer Value: {num} (type: {type(num)})"
)  # Outputs: Integer Value: 1 (type: <class 'int'>)

# List to tuple conversion (explicit)
list_items = [1, 2, 3]
tuple_items = tuple(list_items)  # Explicit conversion of list to tuple
print(
    f"Tuple: {tuple_items} (type: {type(tuple_items)})"
)  # Outputs: Tuple: (1, 2, 3) (type: <class 'tuple'>)

# String to float conversion (explicit)
float_str = "123.45"
float_num = float(float_str)  # Explicit conversion of string to float
print(
    f"Float Value: {float_num} (type: {type(float_num)})"
)  # Outputs: Float Value: 123.45 (type: <class 'float'>)

# Tuple to list conversion (explicit)
tuple_items = (4, 5, 6)
list_items = list(tuple_items)  # Explicit conversion of tuple to list
print(
    f"List: {list_items} (type: {type(list_items)})"
)  # Outputs: List: [4, 5, 6] (type: <class 'list'>)

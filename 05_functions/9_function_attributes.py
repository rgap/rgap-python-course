# In Python, functions can have attributes just like objects. These attributes are stored in the function's __dict__.
# This allows you to store additional information related to a function beyond its code logic.

def my_function():
    print("This is a simple function.")

# Assign an attribute to the function.
my_function.description = "This function prints a message."

# Access the function's attribute.
print(my_function.description)  # Outputs: 'This function prints a message.'

# You can inspect all attributes of the function using its __dict__.
print(my_function.__dict__)  # Outputs the function's attribute dictionary.

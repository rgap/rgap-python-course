# Python Version: Local variables have been a fundamental part of Python since version 1.0 (January 1994).

# A local variable is a variable that is defined within a function or a block of code.
# Local variables are accessible only within the scope of the function or block where they are defined.


def my_function():
    y = 5  # 'y' is a local variable, accessible only within my_function()
    print(f"The value of local variable y is: {y}")


my_function()  # Outputs: The value of local variable y is: 5

# Trying to access 'y' outside the function will raise an error
# Uncomment the line below to see the error
# print(y)  # NameError: name 'y' is not defined

# Note: Local variables are preferable to global variables for their encapsulation and reduced risk of side effects.

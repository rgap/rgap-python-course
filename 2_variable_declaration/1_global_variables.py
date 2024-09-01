# Global Variables in Python
# Python Version: Global variables have been part of Python since its inception in version 1.0 (January 1994).

# A global variable is a variable that is defined outside of any function or class and can be accessed globally.
# Global variables are accessible throughout the entire script, including within functions (unless shadowed by local variables).

# Example of a global variable
x = 10  # 'x' is a global variable


def print_global():
    # Accessing the global variable inside a function
    print(f"The value of global variable x is: {x}")


print_global()  # Outputs: The value of global variable x is: 10


# Modifying global variables within a function
def modify_global():
    global x  # Declare 'x' as global to modify it inside the function
    x = 20


modify_global()
print(
    f"The modified value of global variable x is: {x}"
)  # Outputs: The modified value of global variable x is: 20

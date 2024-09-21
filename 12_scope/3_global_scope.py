# Python Version: Global scope and variable accessibility have been supported since Python 1.0 (January 1994).

# Global Scope in Python
# Variables defined at the top level of a script or module are in the global scope.
# Global variables can be accessed from any part of the code.

# Example of a global variable
global_var = "I am a global variable"


def print_global():
    # Accessing the global variable within a function
    print(global_var)


print_global()  # Outputs: I am a global variable


# Modifying a global variable inside a function
def modify_global():
    global global_var  # Declare the intention to modify the global variable
    global_var = "I have been modified"


modify_global()
print(global_var)  # Outputs: I have been modified

# Note: Global variables are accessible throughout the entire program.
# However, modifying global variables inside functions requires the use of the `global` keyword.
# Excessive use of global variables can lead to code that is difficult to maintain and debug.

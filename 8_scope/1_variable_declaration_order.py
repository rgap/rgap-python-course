# Python Version: Python does not allow the use of variables before they are declared.

# Variable Declaration Order in Python
# In Python, variables must be declared before they are used.


def example():
    # Uncommenting the next line will cause an error because 'a' is used before it is assigned
    # print(a)  # Uncommenting this line will raise UnboundLocalError: local variable 'a' referenced before assignment

    a = 10
    print(a)  # Outputs: 10


example()

# Note: In Python, variables must be declared before they are accessed within a scope.
# Trying to access a variable before it is defined will result in an UnboundLocalError.

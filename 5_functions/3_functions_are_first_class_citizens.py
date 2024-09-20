# 1. Functions in Python can be treated as values and assigned to variables.
def greet(name):
    return f"Hello, {name}!"


# Assigning the greet function to the variable say_hello
say_hello = greet

# Now say_hello can be used as a function.
print(say_hello("Alice"))  # Output: Hello, Alice!


###################################################


# 2. Functions can also be passed as arguments to other functions.
def welcome_message(func, name):
    return func(name)


# Passing the greet function as an argument to welcome_message
print(welcome_message(greet, "Bob"))  # Output: Hello, Bob!


###################################################

# 3. Functions can be returned from other functions.
def get_greeting_func():
    return greet


# Getting a function as the return value and calling it
greet_func = get_greeting_func()
print(greet_func("Charlie"))  # Output: Hello, Charlie!

# In Python, functions are first-class citizens. This means that functions
# can be assigned to variables, passed as arguments to other functions,
# and returned from functions just like any other object. This allows for
# flexible and dynamic programming patterns, such as higher-order functions
# and function decorators.

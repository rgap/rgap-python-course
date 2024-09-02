# ===============================
# VARIABLES
# ===============================

# Not recommended (PEP 8)
# Using single-letter variable names like 'x', 'y', and 'z' is discouraged
# unless the context is extremely clear. PEP 8 advises using descriptive names
# to make the code more readable and self-explanatory.
x = "Maria Gomez"
y, z = x.split()

# Recommended (PEP 8)
# Descriptive variable names like 'name', 'first_name', and 'last_name'
# improve code readability. PEP 8 encourages the use of meaningful names
# that indicate the purpose of the variable.
name = "Maria Gomez"
first_name, last_name = name.split()


# ===============================
# CONSTANTS
# ===============================

# Recommended (PEP 8)
# Constants should be written in uppercase letters with underscores separating
# words, as per PEP 8. This convention helps distinguish constants from variables
# and signals that these values are intended to be immutable.
MAX_VALUE = 10
TOTAL = 30


# ===============================
# FUNCTIONS
# ===============================

# Not recommended (PEP 8)
# PEP 8 advises against using unclear or abbreviated function names like 'db'.
# Function names should be descriptive and written in lowercase with words separated
# by underscores to clearly indicate their purpose.
def db(x):
    return x * 2

# Recommended (PEP 8)
# Function names should be descriptive and follow the lowercase_with_underscores
# convention as per PEP 8. This naming style makes the code more intuitive and easier
# to understand.


def multiply_by_two(x):
    return x * 2


# ===============================
# CLASSES
# ===============================

# Class names should follow the CamelCase convention, as recommended by PEP 8.
# The 'Hero' class is properly named, and its methods and attributes follow
# PEP 8 guidelines, using descriptive names and organizing related functionality
# within the class.
class Hero:
    def __init__(self, name, health, armor, power, weapon):
        # Attribute names should be descriptive, following the lowercase_with_underscores
        # convention as recommended by PEP 8. Each attribute clearly describes
        # its purpose.
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    # Method names should also be descriptive and follow the lowercase_with_underscores
    # convention as per PEP 8. These method names clearly indicate their
    # functionality.
    def print_info(self):
        pass

    def strike_enemy(self, enemy):
        pass


# Constants like 'NUMBER_TO_GUESS' and 'LIVES' follow the PEP 8 recommendation
# of using uppercase letters with underscores for constants.
NUMBER_TO_GUESS = "19"
LIVES = 3

# Variable names like 'lives_played' follow the PEP 8 convention of using
# lowercase_with_underscores, making the code more readable.
lives_played = 0

# The while loop and if statements are structured according to PEP 8 guidelines,
# with proper indentation and clear logic flow.
while lives_played != LIVES:
    # Input prompt message is clear and follows PEP 8 recommendations
    # for string formatting.
    number = input("Adivina el numero: ")

    # The if statement is clear and uses consistent indentation,
    # following PEP 8 guidelines for control structures.
    if number == NUMBER_TO_GUESS:
        print("Ganaste")
        break

    # Increments the 'lives_played' counter, following PEP 8's recommendation
    # for using the += operator in such cases.
    lives_played += 1

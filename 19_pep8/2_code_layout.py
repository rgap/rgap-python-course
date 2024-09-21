# ===============================
# BLANK LINES
# ===============================

# PEP 8 recommends surrounding top-level functions and class definitions
# with two blank lines. This provides a clear visual separation between
# different sections of the code and improves readability.

# ===============================
# CLASS DEFINITIONS
# ===============================

# Two blank lines before this class definition
class MyFirstClass:
    # Surround method definitions inside classes with a single blank line.
    # This separates the methods clearly, making the class easier to read.

    def first_method(self):
        return None

    # One blank line between methods
    def second_method(self):
        return None


# Two blank lines before this class definition
class MySecondClass:
    pass


# ===============================
# FUNCTION DEFINITIONS
# ===============================

# Two blank lines before this function definition
def top_level_function():
    return None


# ===============================
# INSIDE FUNCTIONS
# ===============================

# Use blank lines sparingly inside functions to show clear steps.
# PEP 8 advises using blank lines within a function only when necessary
# to separate different sections or logical steps in the code.

def calculate_variance(number_list):
    # No blank line before initializing the sum_list variable,
    # as these steps are closely related.
    sum_list = 0
    for number in number_list:
        sum_list = sum_list + number

    # One blank line to separate the calculation of the mean
    # from the previous step.
    mean = sum_list / len(number_list)

    # Another blank line to separate the next logical section
    # of the function, which calculates the mean of squares.
    sum_squares = 0
    for number in number_list:
        sum_squares = sum_squares + number**2

    # One blank line before the return statement,
    # separating it from the preceding computations.
    mean_squares = sum_squares / len(number_list)

    return mean_squares - mean**2

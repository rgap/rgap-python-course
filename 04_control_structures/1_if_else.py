# If-Else Statements in Python
# Python Version: The if-else control structure has been part of Python since version 1.0 (January 1994).

# The if-else statement allows you to execute certain code based on a condition.
# It is the most basic form of control flow and is fundamental to decision-making in any program.

x = 10

# Basic if-else structure
# The if block executes if the condition is True.
# If the condition is False, the else block (if present) will execute.
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")  # This block will not execute since x > 5 is True

# The elif keyword allows you to check multiple conditions.
# The first condition that evaluates to True will execute its block of code, and the rest will be ignored.
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print(
        "x is greater than 5 but not greater than 15"
    )  # This block executes since x > 5
else:
    print("x is 5 or less")

# Nested if-else statements
# You can nest if-else statements inside each other to handle complex conditions.
if x > 5:
    if x < 20:
        print("x is between 5 and 20")
    else:
        print("x is 20 or greater")
else:
    print("x is 5 or less")

# Note: Proper use of indentation is critical in Python to define the scope of each block.

# ===============================
# FUNCTION DEFINITIONS
# ===============================

# PEP 8 recommends not having spaces around the equals sign when used to 
# assign a default parameter value in a function definition.
def function(default_parameter=5):
    pass


# ===============================
# ASSIGNMENTS
# ===============================

# PEP 8 recommends using a single space on either side of an assignment operator.
x = 3
y = 2


# ===============================
# PRIORITY IN EXPRESSIONS
# ===============================

# Recommended (PEP 8)
# PEP 8 suggests placing a single space around operators like > and == for better readability.
if x > 5 and x % 2 == 0:
    print("x is larger than 5 and divisible by 2!")

# Not Recommended (PEP 8)
# Avoid omitting spaces around operators. It makes the code harder to read.
if x>5 and x%2 == 0:
    print("x is larger than 5 and divisible by 2!")

# Definitely do not do this! (PEP 8)
# Inconsistent spacing around operators makes the code difficult to read and maintain.
if x >5 and x% 2== 0:
    print("x is larger than 5 and divisible by 2!")


# ===============================
# OPERATIONS
# ===============================

# Recommended (PEP 8)
# Use a single space around operators for better readability, especially in complex expressions.
y = x**2 + 5
z = (x + y) * (x - y)

# Not Recommended (PEP 8)
# Avoid adding unnecessary spaces around operators like ** or within parentheses.
y = x ** 2 + 5
z = (x + y) * (x - y)


# ===============================
# LISTS AND SLICES
# ===============================

# Slicing syntax: Treat the colon as the operator with the lowest priority,
# meaning that it should have no extra space around it, just like other operators.
list[3:4]

# When the expression within the slice is more complex, PEP 8 suggests treating the colon
# as an operator with the lowest priority, and hence no extra space around it.
list[x+1 : x+2]

# In an extended slice, both colons must be surrounded by the same amount of whitespace.
list[3:4:5]
list[x+1 : x+2 : x+3]

# If a slice parameter is omitted, the surrounding spaces are omitted as well.
list[x+1 : x+2 :]

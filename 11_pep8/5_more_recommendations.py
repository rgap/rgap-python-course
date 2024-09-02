# ===============================
# BOOLEAN COMPARISONS
# ===============================

# Don’t compare Boolean values to True or False using the equivalence operator.

# Not recommended (PEP 8)
# Directly comparing a Boolean value to True is unnecessary and less readable.
my_bool = 6 > 5
if my_bool == True:
    print('6 is bigger than 5')

# Recommended (PEP 8)
# Simply using the Boolean value in the condition is more readable and idiomatic.
if my_bool:
    print('6 is bigger than 5')


# ===============================
# EMPTY SEQUENCES IN IF STATEMENTS
# ===============================

# Use the fact that empty sequences are falsy in if statements.

# Not recommended (PEP 8)
# Explicitly checking the length of a sequence is verbose and less readable.
my_list = []
if not len(my_list):
    print('List is empty!')

# Recommended (PEP 8)
# Directly checking the sequence itself is more concise and idiomatic, as empty sequences are falsy.
my_list = []
if not my_list:
    print('List is empty!')


# ===============================
# NONE COMPARISONS
# ===============================

# Use `is not` rather than `not ... is` in if statements.

# Not recommended (PEP 8)
# Using `not ... is` is less readable and can be confusing.
if not x is None:
    print('x exists!')

# Recommended (PEP 8)
# Using `is not` is more readable and clearly indicates the intention.
if x is not None:
    print('x exists!')


# ===============================
# NONE CHECKS
# ===============================

# Don’t use `if x:` when you mean `if x is not None:`.

# Not Recommended (PEP 8)
# Using `if x:` may cause unintended behavior if `x` is a falsy value (e.g., `0`, `''`, `[]`).
if arg:
    # Do something with arg...
    pass

# Recommended (PEP 8)
# Explicitly checking `if x is not None:` ensures that the condition only fails if `x` is actually `None`.
if arg is not None:
    # Do something with arg...
    pass


# ===============================
# STRING METHODS
# ===============================

# Use `.startswith()` and `.endswith()` instead of slicing.

word = 'mycat'

# Not recommended (PEP 8)
# Slicing to check the beginning or end of a string is less readable and less efficient.
if word[:3] == 'cat':
    print('The word starts with "cat"')

# Recommended (PEP 8)
# Using `.startswith()` or `.endswith()` is more readable and efficient.
if word.startswith('cat'):
    print('The word starts with "cat"')
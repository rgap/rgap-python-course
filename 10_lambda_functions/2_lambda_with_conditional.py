# Lambda Functions with Conditional Logic

# Example 1: Check if a number is even or odd
# Conditional logic allows lambdas to make decisions based on input.
# This lambda checks if a number is even or odd.

check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(f"The number 7 is: {check_even_odd(7)}")

##########################################################

# Example 2: Determine if a number is positive, negative, or zero
# Lambdas can handle nested conditionals to produce multiple outcomes.

check_sign = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(f"The number -5 is: {check_sign(-5)}")

##########################################################

# Example 3: Categorize string length
# Use lambdas to classify strings based on their length.
# This example categorizes a string as 'Short', 'Medium', or 'Long'.

check_string_length = lambda s: "Short" if len(s) < 5 else ("Medium" if len(s) < 10 else "Long")
print(f"The string 'hello' is: {check_string_length('hello')}")

##########################################################

# Example 4: Categorize age group
# This lambda categorizes a person’s age into 'Child', 'Teenager', or 'Adult'.

categorize_age = lambda age: "Child" if age < 13 else ("Teenager" if age < 18 else "Adult")
print(f"The age 16 is categorized as: {categorize_age(16)}")

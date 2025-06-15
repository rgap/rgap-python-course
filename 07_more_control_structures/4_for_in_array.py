# The `for-in` loop is commonly used to directly iterate over the elements of an iterable (such as a list, tuple, or string).
# This is more concise than using an index to access each element in the iterable.
# Syntax:
#     for <variable> in <iterable>:
#         <code to execute>

# Example 1: Iterating through a list of customer names and printing a greeting
customers = ["Alice", "Bob", "Charlie", "Dana"]
for customer in customers:
    print(f"Hello, {customer}! Welcome to our store.")


###############################################


# Example 2: Modifying a list of employee names to add their job titles
employees = ["Alice", "Bob", "Charlie"]
titled_employees = []
for employee in employees:
    titled_employees.append(f"{employee} - Software Engineer")
print("Employees with Titles:", titled_employees)

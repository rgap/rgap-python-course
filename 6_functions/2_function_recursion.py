# Python Version: Recursion has been supported in Python since its early versions.

# Function Recursion in Python
# Recursion is a method where a function calls itself to solve smaller instances of the same problem.
# It is particularly useful for problems that can be divided into similar sub-problems.


# Example: Factorial of a number using recursion
def factorial(n):
    # Base case: if n is 1 or 0, return 1 (since 0! = 1 and 1! = 1)
    if n == 1 or n == 0:
        return 1
    # Recursive case: n * factorial of n-1
    else:
        return n * factorial(n - 1)


# Calculate factorial of 5
result = factorial(5)
print(f"Factorial of 5: {result}")  # Outputs: Factorial of 5: 120

# The key to understanding recursion is to recognize the base case, which stops the recursion,
# and the recursive case, which reduces the problem into smaller subproblems.


# Example: Fibonacci series using recursion
def fibonacci(n):
    # Base case: F(0) = 0, F(1) = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Calculate the 6th Fibonacci number
fib_result = fibonacci(6)
print(f"6th Fibonacci number: {fib_result}")  # Outputs: 6th Fibonacci number: 8

# Note: Recursion is elegant and simplifies problems that have a natural recursive structure.
# However, it must be used carefully as deep recursion can lead to performance issues,
# such as excessive memory use or reaching the recursion limit.
# Iterative solutions are often preferred for large-scale problems for efficiency reasons.

# Break and Continue Statements in Python
# Python Version: Break and continue statements have been part of Python since version 1.0 (January 1994).

# Break and continue statements provide control over loop execution, allowing you to exit or skip iterations based on conditions.

# Example: Using break to exit a loop early
for i in range(10):
    if i == 5:
        print("Breaking the loop")
        break  # Exit loop when i is 5
    print(f"i: {i}")

# Example: Using continue to skip an iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the current iteration if i is even
    print(f"Odd i: {i}")

# Nested loops with break
# Break will only exit the innermost loop.
for outer in range(3):
    for inner in range(5):
        if inner == 3:
            print("Breaking inner loop")
            break
        print(f"Outer: {outer}, Inner: {inner}")

# Nested loops with continue
# Continue will only skip the current iteration of the innermost loop.
for outer in range(3):
    for inner in range(5):
        if inner == 3:
            print("Skipping iteration in inner loop")
            continue
        print(f"Outer: {outer}, Inner: {inner}")

# Note: Break and continue are powerful tools for managing loop execution, enabling complex flow control within loops.

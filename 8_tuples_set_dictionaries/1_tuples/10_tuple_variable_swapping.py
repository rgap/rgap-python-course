# Simple Tuple Use Case: Swapping Variables

# Initial values
x, y = 10, 20
# Outputs: Before swapping: x = 10, y = 20
print(f"Before swapping: x = {x}, y = {y}")

# Swapping values using tuple unpacking
x, y = y, x
# Outputs: After swapping: x = 20, y = 10
print(f"After swapping: x = {x}, y = {y}")

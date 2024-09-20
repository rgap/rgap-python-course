# While Loops in Python
# Python Version: The while loop has been part of Python since version 1.0 (January 1994).

# The while loop repeatedly executes a block of code as long as the condition remains True.
# It is useful when the number of iterations is not known beforehand.

# Example: Basic while loop
count = 0

while count < 5:
    print(f"Count: {count}")
    count += 1  # Increment the counter

# Example: Using while loop to sum numbers until a condition is met
total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print(f"Total sum from 1 to 10 is: {total}")  # Outputs: Total sum from 1 to 10 is: 55

# Infinite loop (use with caution)
# An infinite loop runs forever unless externally stopped or broken from within.
# Uncomment the lines below to create an infinite loop
# while True:
#     print("This will run forever")

# Using while loop with a break condition
n = 10
while n > 0:
    print(f"Countdown: {n}")
    n -= 1
    if n == 5:
        print("Breaking the loop")
        break  # Exit the loop when n is 5

# Note: While loops provide flexibility for conditions that depend on dynamic values, but care must be taken to avoid infinite loops.

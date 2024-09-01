# Simulating Do-While Loops in Python
# Python does not have a built-in do-while loop, but similar behavior can be achieved using a while loop.

# A do-while loop guarantees that the loop body will execute at least once before checking the condition.

# Simulating do-while with a while loop
count = 0

while True:
    print(f"Count: {count}")
    count += 1
    if count >= 5:
        break  # Exit the loop

# Note: The loop body executes first, and the condition is checked after, simulating a do-while loop.
# This is useful when you want the loop to run at least once regardless of the condition.

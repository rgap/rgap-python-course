# Introducing `if __name__ == "__main__"` structure.
# This block will only execute if the script is run directly.

print("c_basic_if_main: This always runs.")

if __name__ == "__main__":
    print("c_basic_if_main: This runs only when the script is executed directly.")

# Expected behavior:
# - Run directly: Both print statements will execute.
# - Import: Only the first print statement will execute.

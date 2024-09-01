# Python Version: Block scope in Python is not as strict as in some other languages, but it has been enhanced in Python 3.0 (December 2008) with the introduction of comprehensions.

# Block Scope in Python
# Python does not enforce block-level scope for if, for, and while statements as strictly as other languages.
# However, variables created within these blocks are still accessible after the block ends.

# Example with a for loop
for i in range(5):
    block_var = i
    print(f"Inside block: {block_var}")

print(f"Outside block: {block_var}")  # Outputs: Outside block: 4

# Note: Unlike languages like JavaScript, where variables declared within a block (e.g., inside an if statement or loop) are not accessible outside that block, Python variables defined in blocks are accessible outside the block.
# This can lead to unexpected behavior, so it's important to manage variable names carefully.

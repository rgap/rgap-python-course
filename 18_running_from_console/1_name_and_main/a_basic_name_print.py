# The simplest possible example: Just print `__name__`.
# When this script is run, `__name__` will be "__main__" if executed directly.

print(f"Value of __name__: {__name__}")

# Expected behavior:
# - Run this script directly: `__name__` will be "__main__".
# - Import this script: `__name__` will be "1_basic_name_print".

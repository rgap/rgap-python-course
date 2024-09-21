# Import the module `a_basic_name_print`.
# The `a_basic_name_print` module already has its own namespace, and by importing it, 
# we gain access to the contents of that namespace (functions, variables, etc.).

import a_basic_name_print

# This script imports `a_basic_name_print.py` and shows the value of `__name__` in both scripts.
print(f"In c_basic_import.py, value of __name__: {__name__}")

# Explanation:
# - Each module in Python has its own namespace.
# - The `__name__` variable in this script will be `"__main__"` because this is the main script being executed.
# - The `__name__` variable in `a_basic_name_print` will be set to the module's name (i.e., `a_basic_name_print`), 
#   since it's being imported and not run directly.

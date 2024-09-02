# main.py

# This script should be run from the parent directory of '3_parent_relative_import'.
# Command: $ python -m 3_parent_relative_import.main

# This ensures that Python recognizes 'parent_relative_import' as a package
# and allows the relative import from the parent module to work correctly.

from .subpackage.submodule import greet_combined

print(greet_combined())

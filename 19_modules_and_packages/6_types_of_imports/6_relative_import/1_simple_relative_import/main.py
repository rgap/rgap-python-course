# main.py

# This script should be run from the parent directory of '1_simple_relative_import'.
# Command: $ python -m 1_simple_relative_import.main

# This ensures that Python recognizes 'simple_relative_import' as a package
# and allows the relative import to work correctly.

from .module import greet

print(greet())

# main.py

# This script should be run from the parent directory of '2_relative_import_submodule'.
# Command: $ python -m 2_relative_import_submodule.main

# This ensures that Python recognizes 'relative_import_submodule' as a package
# and allows the relative import from the submodule to work correctly.

from .subpackage.module import greet

print(greet())

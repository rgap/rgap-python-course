# Starting with Python 3.3, the __init__.py file is no longer
# required to treat a directory as a package.
# These are known as "namespace packages," which allow for
# more flexible package structures, especially useful when
# developing large applications with many packages or when
# distributing parts of a package across multiple directories.

# example_using_package.py
# Python Version: Importing from packages has been supported since Python 1.0.

from my_package.module_a import function_a
from my_package.module_b import function_b

print(function_a())  # Outputs: Function A from module_a
print(function_b())  # Outputs: Function B from module_b

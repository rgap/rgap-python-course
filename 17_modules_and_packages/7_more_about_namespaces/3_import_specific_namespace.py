# Instead of importing everything with `import *`, you can import only the specific functions or variables needed.
# This helps avoid namespace pollution and ensures more control over what is brought into the global namespace.

# Importing only the specific 'pi' and 'sqrt' from the math module.
from math import pi, sqrt

# Now we can use these specific names without cluttering the global namespace.
print("Value of pi:", pi)  # Outputs the value of pi.
print("Square root of 16:", sqrt(16))  # Outputs the square root of 16.

# No risk of namespace collision with other math module functions or variables.

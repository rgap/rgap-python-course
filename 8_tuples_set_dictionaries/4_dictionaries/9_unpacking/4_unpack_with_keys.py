# Unpacking specific keys from a dictionary with ** for a math function
def calculate_force(mass, acceleration):
    return mass * acceleration

data = {'mass': 60, 'acceleration': 9.8, 'friction': 0.3}

# Creating a new dictionary with only the needed keys
physics_data = {key: data[key] for key in ['mass', 'acceleration']}

# Unpacking the filtered dictionary
force = calculate_force(**physics_data)
print(f"Force: {force}")  # Output: Force: 588.0

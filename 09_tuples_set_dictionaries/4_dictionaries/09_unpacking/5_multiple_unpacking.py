# Unpacking multiple dictionaries with ** for a math function
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

mass_data = {'mass': 70}
velocity_data = {'velocity': 15}

# Combining dictionaries with **
# if there are duplicate keys, the last one will be used
combined_data = {**mass_data, **velocity_data}

# Unpacking the combined dictionary
ke = calculate_kinetic_energy(**combined_data)
print(f"Kinetic Energy: {ke}")  # Output: Kinetic Energy: 7875.0

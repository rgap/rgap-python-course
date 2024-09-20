# Unpacking with default values using ** for a math function
def calculate_circle_area(radius, pi=3.14159):
    return pi * radius ** 2

circle = {'radius': 7}

# Unpacking the dictionary, with default value for pi
area = calculate_circle_area(**circle)
print(f"Circle Area: {area}")  # Output: Circle Area: 153.93804


################################################


# Example of combining unpacking with other operations for a math function
def calculate_pressure(force, area=1):
    return force / area

data = {'force': 500}

# Unpacking and adding a default area value
pressure = calculate_pressure(**data, area=50)
print(f"Pressure: {pressure}")  # Output: Pressure: 10.0

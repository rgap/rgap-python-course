# Example of unpacking a single dictionary with ** for a math function
def calculate_area(length, width):
    return length * width

dimensions = {'length': 10, 'width': 5}

# Unpacking the dictionary into function arguments
area = calculate_area(**dimensions)
print(f"Area: {area}")  # Output: Area: 50

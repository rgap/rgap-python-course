# Unpacking Multiple Return Values from Functions

def return_multiple():
    return 1, 2, 3


# Unpacking multiple return values
x, y, z = return_multiple()
print(f"x: {x}, y: {y}, z: {z}")  # Outputs: x: 1, y: 2, z: 3

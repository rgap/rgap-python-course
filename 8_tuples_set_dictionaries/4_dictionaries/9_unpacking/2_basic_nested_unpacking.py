# Example of unpacking nested dictionaries for a math function
def calculate_volume(length, width, height):
    return length * width * height

box = {
    'material': 'cardboard',
    'dimensions': {
        'length': 10,
        'width': 5,
        'height': 4
    }
}

# Unpacking the nested 'dimensions' dictionary
volume = calculate_volume(**box['dimensions'])
print(f"Volume: {volume}")  # Output: Volume: 200

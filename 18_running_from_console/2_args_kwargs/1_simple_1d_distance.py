def calculate_1d_distance(x1, x2):
    distance = abs(x2 - x1)
    print(f"The distance between points {
          x1} and {x2} is {distance:.2f} units.")


# This block runs when the script is executed directly.
if __name__ == "__main__":
    calculate_1d_distance(5, 10)

# How to run:
# Run the script directly by typing this in the console:
# $ python 1_simple_1d_distance.py
# This will output: The distance between points 5 and 10 is 5.00 units.

def calculate_1d_distance(*args):
    if len(args) == 2:
        x1, x2 = args
        distance = abs(x2 - x1)
        print(f"The distance between points {
              x1} and {x2} is {distance:.2f} units.")
    else:
        print("Please provide exactly two numbers.")


if __name__ == "__main__":
    # Predefined values for demonstration
    calculate_1d_distance(3, 8)

# How to run:
# Run the script directly by typing this in the console:
# $ python 2_1d_distance_with_args.py
# This will output: The distance between points 3 and 8 is 5.00 units.

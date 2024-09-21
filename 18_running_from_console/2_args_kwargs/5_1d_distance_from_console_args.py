import sys


def calculate_1d_distance(x1, x2):
    distance = abs(x2 - x1)
    print(f"The distance between points {
          x1} and {x2} is {distance:.2f} units.")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x1 = float(sys.argv[1])
        x2 = float(sys.argv[2])
        calculate_1d_distance(x1, x2)
    else:
        print("Please provide exactly two numbers as arguments.")

# How to run:
# Pass two numbers as arguments from the console:
# $ python 5_1d_distance_from_console_args.py 3 9
# This will output: The distance between points 3 and 9 is 6.00 units.

import sys


def calculate_1d_distance(x1, x2):
    # Function to calculate the absolute distance using keyword arguments.
    distance = abs(x2 - x1)
    print(f"The distance between points {
          x1} and {x2} is {distance:.2f} units.")


def parse_args_to_kwargs(args):
    # Function to parse console arguments into keyword arguments.
    kwargs = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=')
            kwargs[key] = float(value)
    return kwargs


if __name__ == "__main__":
    kwargs = parse_args_to_kwargs(sys.argv[1:])
    if "x1" in kwargs and "x2" in kwargs:
        calculate_1d_distance(**kwargs)
    else:
        print("Please provide 'x1' and 'x2' as keyword arguments.")

# How to run:
# Pass 'x1' and 'x2' as keyword arguments from the console:
# $ python 6_1d_distance_from_console_kwargs.py x1=2 x2=8
# This will output: The distance between points 2 and 8 is 6.00 units.

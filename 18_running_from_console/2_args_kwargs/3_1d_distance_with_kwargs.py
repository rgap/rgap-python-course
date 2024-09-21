def calculate_1d_distance(**kwargs):
    if "x1" in kwargs and "x2" in kwargs:
        x1, x2 = kwargs["x1"], kwargs["x2"]
        distance = abs(x2 - x1)
        print(f"The distance between points {
              x1} and {x2} is {distance:.2f} units.")
    else:
        print("Please provide 'x1' and 'x2' as keyword arguments.")


if __name__ == "__main__":
    calculate_1d_distance(x1=2, x2=7)

# How to run:
# Run the script directly by typing this in the console:
# $ python 3_1d_distance_with_kwargs.py
# This will output: The distance between points 2 and 7 is 5.00 units.

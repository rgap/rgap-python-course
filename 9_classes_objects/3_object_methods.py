# Python Version: Object methods, including instance methods, have been supported since Python 1.0.

# Object Methods in Python
# Methods are functions that belong to an object and typically operate on that object's data.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Defining a method to calculate the area of the circle
    def area(self):
        return 3.14159 * (self.radius**2)

    # Defining a method to calculate the circumference of the circle
    def circumference(self):
        return 2 * 3.14159 * self.radius


# Creating an object of the Circle class
my_circle = Circle(5)

# Calling methods on the object
print(
    f"Area of the circle: {my_circle.area()}"
)  # Outputs: Area of the circle: 78.53975
print(
    f"Circumference of the circle: {my_circle.circumference()}"
)  # Outputs: Circumference of the circle: 31.4159

# Note: Methods are similar to functions, but they are defined within a class and are called on instances of that class.
# Methods typically operate on the object's properties, providing behavior specific to that object.

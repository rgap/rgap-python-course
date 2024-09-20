# Example 2: Moderate Detail (Focusing on Intent)


class Calculator:
    """
    A class for basic arithmetic operations.

    Methods:
    - add: Returns the sum of two numbers.
    - subtract: Returns the difference of two numbers.
    """

    def add(self, a, b):
        """
        Add two numbers.

        Parameters:
        a (int or float): First number.
        b (int or float): Second number.

        Returns:
        int or float: Sum of 'a' and 'b'.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract 'b' from 'a'.

        Parameters:
        a (int or float): Number to subtract from.
        b (int or float): Number to subtract.

        Returns:
        int or float: Difference of 'a' and 'b'.
        """
        return a - b


# Example usage
calc = Calculator()
print(calc.add(5, 3))

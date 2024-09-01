# Example 1: Highly Detailed (Stating the Obvious)


class Calculator:
    """
    A simple calculator class that can perform basic arithmetic operations.

    Attributes:
    None

    Methods:
    add(a, b):
        Adds two numbers and returns the result.
    subtract(a, b):
        Subtracts the second number from the first and returns the result.
    """

    def add(self, a, b):
        """
        Adds two numbers together.

        Parameters:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

        Returns:
        int or float: The sum of 'a' and 'b'.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first.

        Parameters:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.

        Returns:
        int or float: The result of 'a' minus 'b'.
        """
        return a - b


# Example usage
calc = Calculator()
print(calc.add(5, 3))  # Should print 8

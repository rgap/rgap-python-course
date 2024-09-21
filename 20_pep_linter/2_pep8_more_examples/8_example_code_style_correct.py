# This script serves as a comprehensive example of PEP 8-compliant code,
# incorporating correct code formatting, commenting, naming conventions,
# and indentation as covered in previous examples.

def calculate_discount(price, discount):
    """
    Calculate the discounted price.

    Parameters:
    price (float): Original price of the item.
    discount (float): Discount percentage.

    Returns:
    float: Price after applying the discount.
    """
    return price * (1 - discount / 100)


# Example usage
original_price = 100.0
discount_percentage = 20.0
discounted_price = calculate_discount(original_price, discount_percentage)
print(f"The discounted price is: {discounted_price:.2f}")

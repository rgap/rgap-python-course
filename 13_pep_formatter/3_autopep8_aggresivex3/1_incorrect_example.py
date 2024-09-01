# This script demonstrates a mixture of PEP 8 violations in code style,
# including poor formatting, unclear variable names, inconsistent indentation,
# and lack of proper comments and docstrings.

def CalcDiscount(P,R):return P*(1-R/100)

originalPrice=100.0
discountPercentage=20.0
DiscountedPrice=CalcDiscount(originalPrice,discountPercentage)
print(f"The discounted price is: {DiscountedPrice}")

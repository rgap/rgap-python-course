# infinity_operations.py

# Special Numeric Values in Python: Infinity

import math

import numpy as np

# Getting Infinity (inf) directly

# Using float constructor
infinity = float("inf")
print(f"Positive infinity using float('inf'): {infinity}")  # Outputs: inf
print()

# Using math.inf constant (Python 3.5+)
infinity_math = math.inf
print(f"Positive infinity using math.inf: {infinity_math}")  # Outputs: inf
print()

# Using NumPy's infinity constant
infinity_np = np.inf
print(f"Positive infinity using np.inf: {infinity_np}")  # Outputs: inf
print()

# Getting Negative Infinity directly

# Using float constructor
neg_infinity = float("-inf")
print(f"Negative infinity using float('-inf'): {neg_infinity}")  # Outputs: -inf
print()

# Using math.inf constant negated
neg_infinity_math = -math.inf
print(f"Negative infinity using -math.inf: {neg_infinity_math}")  # Outputs: -inf
print()

# Using NumPy's negative infinity constant
neg_infinity_np = -np.inf
print(f"Negative infinity using -np.inf: {neg_infinity_np}")  # Outputs: -inf
print()

# Getting Infinity (inf) through operations

# Division by zero (positive number)
try:
    infinity = 1.0 / 0.0  # This will raise an error in normal circumstances
except ZeroDivisionError:
    infinity = float("inf")
print(f"Positive infinity by division: {infinity}")  # Outputs: inf
print()

# Negative infinity by dividing a negative number by zero
try:
    neg_infinity = -1.0 / 0.0  # This will raise an error in normal circumstances
except ZeroDivisionError:
    neg_infinity = float("-inf")
print(f"Negative infinity by division: {neg_infinity}")  # Outputs: -inf
print()

# Exponentiation with a large number (conceptual)
large_number = 1e308
infinity_exp = large_number * large_number  # This results in infinity
print(f"Infinity by large number multiplication: {infinity_exp}")  # Outputs: inf
print()

# Operations with Infinity
print(f"Infinity + 1: {infinity + 1}")  # Outputs: inf
print()

print(f"Infinity - 1000: {infinity - 1000}")  # Outputs: inf
print()

print(f"Infinity * 2: {infinity * 2}")  # Outputs: inf
print()

print(f"Infinity / 2: {infinity / 2}")  # Outputs: inf
print()

print(f"Infinity + Infinity: {infinity + infinity}")  # Outputs: inf
print()

print(
    f"Infinity - Infinity: {infinity - infinity}"
)  # Outputs: nan (Indeterminate form)
print()

print(f"Infinity * 0: {infinity * 0}")  # Outputs: nan (Indeterminate form)
print()

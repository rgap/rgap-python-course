# nan_operations.py

# Special Numeric Values in Python: NaN (Not a Number)

import math

import numpy as np

# Getting NaN (Not a Number) directly

# Using float constructor
nan = float("nan")
print(f"NaN using float('nan'): {nan}")  # Outputs: nan
print()

# Using math.nan constant (Python 3.5+)
nan_math = math.nan
print(f"NaN using math.nan: {nan_math}")  # Outputs: nan
print()

# Using NumPy's NaN constant
nan_np = np.nan
print(f"NaN using np.nan: {nan_np}")  # Outputs: nan
print()

# Getting NaN through operations

# Square root of a negative number (normally raises a ValueError)
try:
    nan_sqrt = math.sqrt(
        -1.0
    )  # This would raise a ValueError normally, NaN conceptually
except ValueError:
    nan_sqrt = float("nan")
print(f"NaN by square root of negative: {nan_sqrt}")  # Outputs: nan
print()

# 0 divided by 0 (normally raises ZeroDivisionError)
try:
    nan_div = 0.0 / 0.0  # This will raise an error in normal circumstances
except ZeroDivisionError:
    nan_div = float("nan")
print(f"NaN by division 0/0: {nan_div}")  # Outputs: nan
print()

# Infinity minus infinity
infinity = float("inf")
nan_subtract = infinity - infinity
print(f"NaN by subtracting infinity from infinity: {nan_subtract}")  # Outputs: nan
print()

# 0 multiplied by infinity
nan_multiply = 0.0 * infinity
print(f"NaN by multiplying 0 by infinity: {nan_multiply}")  # Outputs: nan
print()

# Operations with NaN
print(f"NaN + 1: {nan + 1}")  # Outputs: nan
print()

print(f"NaN - 1000: {nan - 1000}")  # Outputs: nan
print()

print(f"NaN * 2: {nan * 2}")  # Outputs: nan
print()

print(f"NaN / 2: {nan / 2}")  # Outputs: nan
print()

print(f"NaN + Infinity: {nan + infinity}")  # Outputs: nan
print()

print(f"NaN - Infinity: {nan - infinity}")  # Outputs: nan
print()

print(f"NaN * Infinity: {nan * infinity}")  # Outputs: nan
print()

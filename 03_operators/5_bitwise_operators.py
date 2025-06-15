# Bitwise Operators in Python
# Python Version: Bitwise operators have been part of Python since version 1.0 (January 1994).

# Bitwise operators allow you to perform operations on the binary representations of integers.
# These operators treat the numbers as a sequence of bits (binary digits) rather than as decimal or hexadecimal values.
# The fundamental bitwise operations include AND, OR, XOR, NOT, and bit shifts (left and right shifts).

# Understanding binary numbers:
# A binary number system uses two symbols, 0 and 1, to represent values. Each digit in a binary number is called a bit.
# For example, the binary number 1100 represents the decimal value 12, and 1010 represents the decimal value 10.

# Assigning binary values to variables:
a = 0b1100  # Binary for 12
b = 0b1010  # Binary for 10

# Note: Bitwise operations work the same way whether the numbers are provided in binary, decimal, or hexadecimal.
# For example, the following operations with decimal integers would yield the same results:
# a = 12  # Decimal for 0b1100
# b = 10  # Decimal for 0b1010

# AND Operator (&):
# The bitwise AND operator compares each bit of its operands. If both bits are 1, the corresponding result bit is set to 1.
# Otherwise, the result bit is set to 0.
# Truth Table for AND:
#   a  b  a & b
#   0  0    0
#   0  1    0
#   1  0    0
#   1  1    1
print(f"a & b: {bin(a & b)}")  # Outputs: 0b1000 (Binary for 8)

# OR Operator (|):
# The bitwise OR operator compares each bit of its operands. If at least one of the bits is 1, the corresponding result bit is set to 1.
# Otherwise, the result bit is set to 0.
# Truth Table for OR:
#   a  b  a | b
#   0  0    0
#   0  1    1
#   1  0    1
#   1  1    1
print(f"a | b: {bin(a | b)}")  # Outputs: 0b1110 (Binary for 14)

# XOR Operator (^):
# The bitwise XOR operator (exclusive OR) compares each bit of its operands. If the corresponding bits of its operands differ, the result bit is set to 1.
# If the corresponding bits are the same, the result bit is set to 0.
# Truth Table for XOR:
#   a  b  a ^ b
#   0  0    0
#   0  1    1
#   1  0    1
#   1  1    0
print(f"a ^ b: {bin(a ^ b)}")  # Outputs: 0b0110 (Binary for 6)

# NOT Operator (~):
# The bitwise NOT operator is a unary operator that inverts all the bits of its operand.
# It flips each bit of the operand: 0 becomes 1, and 1 becomes 0.
# This operation also considers the signed nature of the integer in Python, resulting in a two's complement.
# The formula for the two's complement is: ~x = -x - 1
print(f"~a: {bin(~a)}")  # Outputs: -0b1101 (Binary for -13)

# Left Shift Operator (<<):
# The bitwise left shift operator shifts the bits of the first operand to the left by the number of positions specified by the second operand.
# Each shift to the left multiplies the number by 2. The bits that are shifted out are discarded, and the vacant positions on the right are filled with 0s.
# For example, shifting 0b1100 (12) to the left by 2 positions results in 0b110000 (48).
print(f"a << 2: {bin(a << 2)}")  # Outputs: 0b110000 (Binary for 48)

# Right Shift Operator (>>):
# The bitwise right shift operator shifts the bits of the first operand to the right by the number of positions specified by the second operand.
# Each shift to the right divides the number by 2 (using integer division).
# The bits that are shifted out are discarded, and the vacant positions on the left are filled with the sign bit (for signed integers) or 0 (for unsigned integers).
# For example, shifting 0b1100 (12) to the right by 2 positions results in 0b0011 (3).
print(f"a >> 2: {bin(a >> 2)}")  # Outputs: 0b0011 (Binary for 3)

# Note: All these operations can also be performed using integers directly without converting them to binary first:
# For example:
# print(f"a & b: {a & b}")  # Outputs: 8
# print(f"a | b: {a | b}")  # Outputs: 14
# print(f"a ^ b: {a ^ b}")  # Outputs: 6
# print(f"~a: {~a}")        # Outputs: -13
# print(f"a << 2: {a << 2}")  # Outputs: 48
# print(f"a >> 2: {a >> 2}")  # Outputs: 3

# Bitwise operations are often used in low-level programming, such as in systems programming, cryptography, network protocols, and performance optimization.
# They allow efficient manipulation of data at the bit level, which is essential in scenarios requiring fine-grained control over binary data.

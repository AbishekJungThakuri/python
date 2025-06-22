# There are primarily five ways of rounding off decimals in NumPy:
# truncation
# fix
# rounding
# floor
# ceil

# Truncation
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

import numpy as np


arr = np.trunc([-3.1666, 3.6667])
print(arr)


# fix()
arr1 = np.fix([-3.1666, 3.6667])
print(arr1)

# Rounding
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
# E.g. round off to 1 decimal point, 3.16666 is 3.2

arr2 = np.around(3.1666, 3)
print(arr2)


# FLoor
arr3 = np.floor([-3.1666, 3.6667])
print(arr3)


# Ceil
arr4 = np.ceil([-3.1666, 3.6667])
print(arr4)
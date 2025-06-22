import numpy as np

#  Addition

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

sum = np.add(arr1,arr2)
print(sum)

# Subtraction
sub = np.subtract(arr2,arr1)
print(sub)

# Multiplication
mul = np.multiply(arr1,arr2)
print(mul)

# Division
div = np.divide(arr2,arr1)
print(div)

# REmainder
# Both mod() and remainder() function return remainder


# Quotient and Mod
# The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.

# Absolute Values
# Both the absolute() and the abs() functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()
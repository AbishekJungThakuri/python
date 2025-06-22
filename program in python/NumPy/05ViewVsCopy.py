# Main difference between a copy and a view of an array is that the copy is a
# new array and the view is just a view of the original array.

# Copy doesnt affect the original array but the view will affect the original array.


import numpy as np


# Example for copy, Change the original array and display both arrays:
arr = np.array([1,2,3,4,5])

x = arr.copy()
arr[0] = 10
print(arr)
print(x)

# The copy SHOULD NOT be affected by the changes made to the original array.


# EXample for view
arr1 = np.array([1, 2, 3, 4, 5])
y = arr1.view()
arr1[0] = 41
print(arr1)
print(y)
# The view SHOULD be affected by the changes made to the original array.

print(x.base)
print(y.base)
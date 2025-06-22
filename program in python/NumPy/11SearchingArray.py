# We can search an array for a certain value, and return the indexes that get a match
# To search an array,  use the where() method.

import numpy as np

arr = np.array([1,2,3,4,5,4,4])

x =  np.where(arr == 4)
print(x)  # return a tuple: array([3,5,6])


# Finding the indexes where values are even:

arr1 = np.array([1,2,3,4,5,6,7,8])
y = np.where(arr1%2 == 0)

print(y)

# searchsorted()
# performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

# Finding the indexes of 7

z = np.searchsorted(arr1,7)
print(z)
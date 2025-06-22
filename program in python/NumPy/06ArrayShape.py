# The shape of an array is the number of elements in each dimension.

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr.shape)

arr1 = np.array([1,2,3,4,5], ndmin=5)

print(arr1)
print('Shape of array:', arr.shape)
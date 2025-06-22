# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, we filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.

import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

print(arr[x])


# Creating a filter array that will return value higher than 42:

arr1 = np.array([20,40,110,42,45,66,100])

filter_arr = []

for i in arr1:
    if i > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr1[filter_arr]
print(newarr)


# Creating filter Directly from Array

filter_arr2 = arr1 > 45

newarr1 = arr1[filter_arr2]
print(newarr1)
        
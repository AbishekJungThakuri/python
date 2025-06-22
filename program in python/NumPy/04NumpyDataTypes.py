import numpy as np

arr = np.array([1, 2, 3, 4])
arr1 = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)
print(arr1.dtype)


# Create an array with data type string
arr2 = np.array([1, 2, 3, 4], dtype='S')

print(arr2)
print(arr2.dtype)


# Best way to convert data types
arr3 = np.array([1.1, 2.1, 3.1])

newarr = arr3.astype('i')

print(newarr)
print(newarr.dtype)
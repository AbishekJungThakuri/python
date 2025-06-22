import numpy as np

# print(np.__version__)

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))

# 0-D Arrays
arr1 = np.array(42)
print(arr1)

#  1-D Arrays
arr2 = np.array([3,4,5,8,9])
print(arr2)


# 2-D Arrays  : matrix or 2nd order tensors
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)

# 3-D Arrays : 3rd order tensor
arr4 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr4)


# Checking number of dimensions : ndim

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)


# Creating an array with 5 dimensions 
arr5 = np.array([1,2,3,4,5],ndmin=5)
print(arr5)
print('Number of dimensions :', arr5.ndim)
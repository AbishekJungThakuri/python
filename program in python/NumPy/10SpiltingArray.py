#  We use array_split() for splitting arrays

import numpy as np

arr = np.array([1,2,3,4,5,6])

#  splitting the array in 3 parts:
newarr = np.array_split(arr,3)
print(newarr)

# Accessing the splitted arrays:
print(newarr[0])
print(newarr[1])
print(newarr[2])

#  splitting the array in 4 parts
newarr1 = np.array_split(arr,4)
print(newarr1)


# Splitting 2-D Arrays
arr1 = np.array([[1,2],[2,3],[4,5],[6,7],[7,8],[9,10],[10,11]])
newarr2 = np.array_split(arr1, 3)
print(newarr2)
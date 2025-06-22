# iterating means going through elements one by one.

# Iterating 1-D array:

import numpy as np

arr = np.array([1,2,3,4,5])

# for i in arr:
#     print(i)



# iterating 2-D array:

arr1 = np.array([[1,2,3,4],[5,6,7,8]])

# for j in arr1:
#     print(j)

#Iterate on each scalar element of the 2-D array
# for j in arr1:
#     for k in j:
#         print(k)



# iterating 3-D array:
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for x in arr2:
#   for y in x:
#     for z in y:
#       print(z)


# Iterating Arrays using nditer()

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr3):
#   print(x)


# op_dtypes = change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']

arr4 = np.array([1,2,3])

# for x in np.nditer(arr4, op_dtypes=['S'], flags=['buffered']):
#     print(x)


# Iterating with different steps

arr5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for x in np.nditer(arr5[:, ::3]):
#     print(x)


# Enumerated iteration using ndenumerate()
# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

for index, x in np.ndenumerate(arr):
    print(index, x)
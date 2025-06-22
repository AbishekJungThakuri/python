import numpy as np

arr = np.array([1,2,3,4,5])

print(arr[0])
print(arr[2] + arr[3] )

# Access 2-D arrays
arr1 = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
print(arr1[1,1])
print('5th element on 1st row: ', arr1[0, 4])

# Negative Indexing
print('Last element from 2nd dim: ', arr1[1, -1])
print('Second last element from 2nd dim: ', arr1[1, -2])


# Access 3_D arrays
arr2 = np.array([[[1, 2, 3],[4, 5, 6]], 
                 [[7, 8, 9], [10, 11, 12]]])

print(arr2[0, 1, 2])


# Example Explained
# arr[0, 1, 2] prints the value 6.

# And this is why:

# The first number represents the first dimension, which contains two arrays:
# [[1, 2, 3], [4, 5, 6]]
# and:
# [[7, 8, 9], [10, 11, 12]]
# Since we selected 0, we are left with the first array:
# [[1, 2, 3], [4, 5, 6]]

# The second number represents the second dimension, which also contains two arrays:
# [1, 2, 3]
# and:
# [4, 5, 6]
# Since we selected 1, we are left with the second array:
# [4, 5, 6]

# The third number represents the third dimension, which contains three values:
# 4
# 5
# 6
# Since we selected 2, we end up with the third value:
# 6




# Reshaping means changing the shape of an array

# Reshape from 1-D to 2-D

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(4,3)  # 4 arrays, each with 3 elements
print(newarr)


# Reshape from 1-D to 3-D

newarr1 = arr.reshape(2,3,2)  # 2 arrays that contains 3 arrays, each with 2 elements
print(newarr1)



# Flattening the arrays
#  It means converting a multidimensional array into a 1D array.
#  We can use reshape(-1) to do this.

arr1 = np.array([[1,2,3],[4,5,6]])

newarr2 = arr.reshape(-1)
print(newarr2)
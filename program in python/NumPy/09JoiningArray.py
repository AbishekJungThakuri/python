# joining two arrays using concatenate()

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))
print(arr)


# Joining tw0 2-D arrays along rows(axis = 1)
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

newarr = np.concatenate((arr3,arr4), axis=1)
print(newarr)


# Joining Arrays Using Stack Functions
# tacking is same as concatenation, the only difference is that stacking is done along a new axis.

newarr2 = np.stack((arr1,arr2),axis=1)
print(newarr2)


# stacking ALong Rows:  hstack()
newarr3 = np.hstack((arr1,arr2))
print(newarr3)

# stacking ALong columns:  vstack()
newarr4 = np.vstack((arr1,arr2))
print(newarr4)


# stacking ALong height(depth):  dstack()
newarr5 = np.dstack((arr1,arr2))
print(newarr5)


# Addition is done between two arguments whereas summation happens over n elements.



import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

sum = np.sum([arr1 , arr2])
print(sum)


# Summation Over an Axis
# If you specify axis=1, NumPy will sum the numbers in each array

sum1 = np.sum([arr1,arr2],axis=1)
print(sum1)


# Cummulative Sum
# Cummulative sum means partially adding the elements in array.
# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

arr1 = np.array([1,2,3,4,5])
result = np.cumsum(arr1)
print(result)
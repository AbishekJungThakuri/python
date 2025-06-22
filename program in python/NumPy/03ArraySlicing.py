# slicing means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1


import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])  # Note: The result includes the start index, but excludes the end index.

print(arr[4:])   # Slice elements from index 4 to the end of the array
print(arr[:4])   # Slice elements from the beginning to index 4 (not included)


# Negative Slicing
print(arr[-3:-1])  # start from -3 and end at -1


# using Steps
print(arr[1:5:2])


# slicing 2-D Arrays
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr1[1, 1:4])
print(arr1[0:2, 2])    # From both elements, return index 2
print(arr1[0:2, 1:4])
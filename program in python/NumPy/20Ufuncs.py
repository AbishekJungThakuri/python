# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# Converting iterative statements into a vector based operation is called vectorization.

import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x,y)

print(z)



# To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
# The frompyfunc() method takes the following arguments:
# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.



# Creating own ufunc for addition:

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd,2,1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
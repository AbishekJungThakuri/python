# Logs
# NumPy provides functions to perform log at the base 2, e and 10.
# We will also explore how we can take log for any base by creating a custom ufunc.
# All of the log functions will place -inf or inf in the elements if the log can not be computed.


import numpy as np

# Finding log at base 2 of all elements of following array
arr = np.arange(1,10)  #arange(1, 10) function returns an array with integers   starting from 1 (included) to 10 (not included).
print(np.log2(arr))



# Finding log at base 10 of all elements of following array
print(np.log10(arr))


# Use the log() function to perform log at the base e.
print(np.log(arr))


# Log at Any Base
# NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:


from math import log

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100,15))   # here 15 is base and 100 is value



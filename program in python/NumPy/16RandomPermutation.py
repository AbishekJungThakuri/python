# A permutations refers to an arrangement of elements. E.g. [3,2,1] is a permutation of [1,2,3] and vice versa.

# The NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.

import numpy as np
from numpy import random

# Randomly shuffle elements:
arr = np.array([1,2,3,4,5]);
random.shuffle(arr)
print(arr)


# random permutation of elements:
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
x = random.permutation(arr)
print(x)



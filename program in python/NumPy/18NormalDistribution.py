# use the random.normal() method to get a Normal Data Distribution.
# It has three parameters:
# loc - (Mean) where the peak of the bell exists.
# scale - (standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array

from numpy import random

x = random.normal(size=(2,3))
print(x)

# random normal distribution of size 2x3 with mean at 1 and standard deviation of 2

y = random.normal(loc=1, scale=2, size=(2,3))
print(y)

# Visualization of Normal Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000))
plt.show()
#  Seaborn is a library that uses Matplotlib underneath to ploat graphs.It willbe used to visualize random distributions.

# Distplots stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

# Plotting a Distplot

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0,1,2,3,4,5])

plt.show()
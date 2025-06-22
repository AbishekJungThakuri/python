import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1,num2)
print(x)

# Finding LCM in Arrays
# To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.

arr = np.array([3,6,9])

x = np.lcm.reduce(arr)
print(x)


# Lcm from 1 to 10:

range = np.arange(1,11)
y = np.lcm.reduce(range)
print(y)



#  Gcd is also done same as lcm
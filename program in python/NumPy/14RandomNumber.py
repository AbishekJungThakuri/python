from numpy import random

# random integer from 0 to 100
x = random.randint(100)
print(x)

# random float from 0 to 1:
y = random.rand()
print(y)


# Generating a 1-D array containing 5 random integers from 0 to 100:
z = random.randint(100, size=5 )
print(z)


# Generating a 2-d array with 3 rows containing 5 integers:
a = random.randint(100, size=(3,5))
print(a)


# Choice() method allows you to generate a random value based on an array of values.
#  It takes array as a parameter and randomly returns one of the values.

c = random.choice([3,4,7,9])
print(c)
import pandas as pd

a = [1, 7, 2]

result = pd.Series(a)
print(result)
print(result[0])

result1 = pd.Series(a, index=['x','y','z'])
print(result1)

# Accessing value from created label
print(result1['z'])


# key/value objects as series
# You can also use a key/value object, like a dictionary, when creating a Series.

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

result3 = pd.Series(calories)
print(result3)

# Note: The keys of the dictionary becomes labels.
# To select only some of the items in dictionary, use the index argument and specify only the items you want to include in the Series.

result4 = pd.Series(calories, index=["day1","day2"])
print(result4)


# DataFrames

# Creating a DataFrame from two Series:

data = {
    "calories": [200,300,390],
    "duration": [40,30,45]
}

myvar = pd.DataFrame(data)
print(myvar)
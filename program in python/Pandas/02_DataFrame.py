# Pandas DataFrame is a 2 dimensional data structure, like a 2D array, or a table with rows and columns

# Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

# Locate Row

# Return row 0:
print(df.loc[0])

# Return row 0 and 1:
print(df.loc[[0,1]])

# Note: when using [], the result is a pandas DataFrame.

# Named Indexes
# With the index argument, you can name your own indexes.

df1 = pd.DataFrame(data, index=["day1","day2","day3"])
print(df1)


# Load Files into a DataFrame
# If your data sets are stored in a file, Pandas can load them into a DataFrame.

# df2 = pd.read_csv('data.csv')
# print(df2)
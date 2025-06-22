# Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')
# print(df.head(10))

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.


# Print the first 5 rows of the DataFrame:
# print(df.head())


# tail() method

# Print the last 5 rows of the DataFrame:
# print(df.tail()) 


# info(), that gives you more information about the data set.
print(df.info()) 
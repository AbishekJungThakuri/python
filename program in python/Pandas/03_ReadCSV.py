import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.to_string())   # use to_string() to print the entire DataFrame

# Print The DataFrame without the to_string() Method
# print(df)


# max_rows

print(pd.options.display.max_rows)

pd.options.display.max_rows = 200

df = pd.read_csv('data.csv')

print(df) 
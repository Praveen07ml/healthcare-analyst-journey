

#loading csv file

import pandas as pd

df = pd.read_csv("startup_funding.csv")



# load and understanding Size

print(f"{df.shape[0]} rows")
print(f"{df.shape[1]} columns")
print(f"{df.shape[0] * df.shape[1]} Total Data points")


# understanding columns


for i,col in enumerate(df.columns):
    print(f"{i+1} - {col}")

# seeing the actual data

print(df.head())  # top  5 rows
print(df.tail()) # last 5 rows
print(df.sample(10)) # random10rows

# understand the data types


print(df.dtypes)

print(df.info())
import pandas as pd
import re

# import data
df = pd.read_csv('day2.txt', sep=" ", header=None)
df.columns = ["minmax", "letter", "password"]

# clean data
df['min'] = ''
df['max'] = ''
df['letter_cleaned'] = df['letter'].str[:1]

# df.dtypes

# script for checking password

accepted = []
not_accepted = []

for index, row in df.iterrows():

    row['min'] = int(re.split(r'[\-]', row['minmax'])[0])
    row['max'] = int(re.split(r'[\-]', row['minmax'])[1])

    conditions = [(row['password'][row['min']-1] == row['letter_cleaned']),
                  (row['password'][row['max']-1] == row['letter_cleaned'])]

    if any(conditions) and not all(conditions):
        accepted.append(index)

    else:
        not_accepted.append(index)

print(len(accepted))
print(accepted)
print(df['min'].unique())
print(df.tail(15))

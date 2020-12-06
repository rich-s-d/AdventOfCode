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

    password = row['password']
    occurance = password.count(row['letter_cleaned'])

    if row['letter_cleaned'] in row['password']:
        if occurance <= row['max'] and occurance >= row['min']:
            accepted.append(index)

    else:
        not_accepted.append(index)

print(len(accepted))
print(accepted)
print(df['min'].unique())
print(df.tail(15))

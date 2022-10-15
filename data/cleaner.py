import ast
import pandas as pd
import re
import operator
from itertools import islice
import csv

import json
import topojson

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))







df = pd.read_csv('data/global firepower 2022 wide.csv', usecols=['country', 'Tanks'])

print(df.head())

country = df['country'].tolist()
Tanks = df['Tanks'].tolist()


TanksD = dict()


for index, row in df.iterrows():
    if row['Tanks'] > 2830:
        TanksD[row['country']] = row['Tanks']





TanksD2 = dict()

for key in TanksD:
    TanksD2[key] = range(1000, TanksD[key], 1000)






#print(gold_count)
#print(silver_count)
#print(bronze_count)

big_dict = []
for key in TanksD2:
    for val in TanksD2[key]:
        big_dict.append({
            "country": key,
            "Tanks": val/1000,
    })



fields = ['country', 'Tanks']
with open('data/tanks_count.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(big_dict)
    
print('Done')
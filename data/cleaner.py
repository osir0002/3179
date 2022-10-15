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







df = pd.read_csv('data/global firepower 2022 wide.csv', usecols=['country', 'Helicopters'])

print(df.head())

country = df['country'].tolist()
Helicopters = df['Helicopters'].tolist()


HelisD = dict()

intervals = 300


for index, row in df.iterrows():
    if  row['Helicopters'] > 310:
        HelisD[row['country']] = row['Helicopters']





HelisD2 = dict()

for key in HelisD:
    HelisD2[key] = range(intervals, HelisD[key], intervals)






#print(gold_count)
#print(silver_count)
#print(bronze_count)

big_dict = []
for key1, key2 in zip(HelisD, HelisD2):
    for val in HelisD2[key2]:
        big_dict.append({
            "country": key2,
            "HeliCount": val/intervals,
            "Helicopters": HelisD[key1]
    })



fields = ['country', 'HeliCount', 'Helicopters']
with open('data/heli_count.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(big_dict)
    
print('Done')
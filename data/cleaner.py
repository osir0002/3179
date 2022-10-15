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







df = pd.read_csv('data/global firepower 2022 wide.csv', usecols=['country', 'Navy_Ships'])

print(df.head())

country = df['country'].tolist()
Navy_Ships = df['Navy_Ships'].tolist()


ShipsD = dict()

intervals = 100


for index, row in df.iterrows():
    if  row['Navy_Ships'] > 270:
        ShipsD[row['country']] = row['Navy_Ships']





ShipsD2 = dict()

for key in ShipsD:
    ShipsD2[key] = range(intervals, ShipsD[key], intervals)






#print(gold_count)
#print(silver_count)
#print(bronze_count)

big_dict = []
for key1, key2 in zip(ShipsD, ShipsD2):
    for val in ShipsD2[key2]:
        big_dict.append({
            "country": key2,
            "ShipCount": val/intervals,
            "Ships": ShipsD[key1]
    })



fields = ['country', 'ShipCount', 'Ships']
with open('data/heli_count.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(big_dict)
    
print('Done')
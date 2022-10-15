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







df = pd.read_csv('data/global firepower 2022 wide.csv', usecols=['country', 'Dedicated_Attack', 'Fighters/Interceptors'])

print(df.head())

country = df['country'].tolist()
Fighters = df['Fighters/Interceptors'].tolist()


PlanesD = dict()

intervals = 1000


for index, row in df.iterrows():
    if  row['Fighters/Interceptors'] > 1000:
        PlanesD[row['country']] = row['Fighters/Interceptors']





PlanesD2 = dict()

for key in PlanesD:
    PlanesD2[key] = range(intervals, PlanesD[key], intervals)






#print(gold_count)
#print(silver_count)
#print(bronze_count)

big_dict = []
for key1, key2 in zip(PlanesD, PlanesD2):
    for val in PlanesD2[key2]:
        big_dict.append({
            "country": key2,
            "PlanesCount": val/intervals,
            "Planes": PlanesD[key1]
    })



fields = ['country', 'PlanesCount', 'Planes']
with open('data/planes_count.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(big_dict)
    
print('Done')
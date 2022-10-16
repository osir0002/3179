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







df = pd.read_csv('data/global firepower 2022 wide.csv', usecols=['country', 'Defense_Budget'])

print(df.head())

country = df['country'].tolist()
Defense_Budget = df['Defense_Budget'].tolist()


MoneyD = dict()

intervals = 40000000000


for index, row in df.iterrows():
    if  int(row['Defense_Budget']) > 42000000000:
        MoneyD[row['country']] = int(row['Defense_Budget'])





MoneyD2 = dict()

for key in MoneyD:
    MoneyD2[key] = range(intervals, MoneyD[key], intervals)






#print(gold_count)
#print(silver_count)
#print(bronze_count)

big_dict = []
for key1, key2 in zip(MoneyD, MoneyD2):
    for val in MoneyD2[key2]:
        big_dict.append({
            "country": key2,
            "MoneyCount": val/intervals,
            "Budget": MoneyD[key1]
    })



fields = ['country', 'MoneyCount', 'Budget']
with open('data/budget_count.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(big_dict)
    
print('Done')
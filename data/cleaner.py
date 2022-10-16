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







df = pd.read_csv('data/rankings.csv')#, usecols=['Country', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022' ])

print(df.head())


"""
country = df['country'].tolist()
Helicopters = df['Helicopters'].tolist()


HeliD = dict()

intervals = 300


for index, row in df.iterrows():
    if  row['Helicopters'] > 300:
        HeliD[row['country']] = row['Helicopters']





HeliD2 = dict()

for key in HeliD:
    HeliD2[key] = range(intervals, HeliD[key], intervals)






#print(gold_count)
#print(silver_count)
#print(bronze_count)

big_dict = []
for key1, key2 in zip(HeliD, HeliD2):
    for val in HeliD2[key2]:
        big_dict.append({
            "country": key2,
            "HeliCount": val/intervals,
            "Helicopters": HeliD[key1]
    })



fields = ['country', 'HeliCount', 'Helicopters']
with open('data/heli_count.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(big_dict)
    
print('Done')
"""

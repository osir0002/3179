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







df = pd.read_csv('data/Nuclear_warheads 1945-2022 per country.csv')#, usecols=['country', 'Defense_Budget'])

print(df.head())

Year = df['Year'].tolist()
United_States = df['United States'].tolist()
Russia = df['Russia'].tolist()
United_Kingdom = df['United Kingdom'].tolist()
France = df['France'].tolist()
China = df['China'].tolist()
Israel = df['Israel'].tolist()
India = df['India'].tolist()
Pakistan = df['Pakistan'].tolist()
North_Korea = df['North Korea'].tolist()


NukesD = dict()
big_dict = []


#intervals = 40000000000


for index, row in df.iterrows():
    #if  int(row['Defense_Budget']) > 42000000000:
    #    NukesD[row['country']] = int(row['Defense_Budget'])

    big_dict.append({
        "Country": "United States of America",
        "Year": row["Year"],
        "Nukes": row["United States"]
    })

    big_dict.append({
        "Country": "Russia",
        "Year": row["Year"],
        "Nukes": row["Russia"]
    })

    big_dict.append({
        "Country": "United Kingdom",
        "Year": row["Year"],
        "Nukes": row["United Kingdom"]
    })

    big_dict.append({
        "Country": "France",
        "Year": row["Year"],
        "Nukes": row["France"]
    })

    big_dict.append({
        "Country": "China",
        "Year": row["Year"],
        "Nukes": row["China"]
    })

    big_dict.append({
        "Country": "Israel",
        "Year": row["Year"],
        "Nukes": row["Israel"]
    })

    big_dict.append({
        "Country": "India",
        "Year": row["Year"],
        "Nukes": row["India"]
    })

    big_dict.append({
        "Country": "Pakistan",
        "Year": row["Year"],
        "Nukes": row["Pakistan"]
    })

    big_dict.append({
        "Country": "North Korea",
        "Year": row["Year"],
        "Nukes": row["North Korea"]
    })

    
    






#NukesD2 = dict()

#for key in NukesD:
#    NukesD2[key] = range(intervals, NukesD[key], intervals)






#print(gold_count)
#print(silver_count)
#print(bronze_count)

# for key1, key2 in zip(NukesD, NukesD2):
#     for val in NukesD2[key2]:
#         big_dict.append({
#             "country": key2,
#             "MoneyCount": val/intervals,
#             "Budget": NukesD[key1]
#     })





fields = ['Country', 'Year', 'Nukes']
with open('data/nukes_data.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(big_dict)
    
print('Done')
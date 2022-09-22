import ast
import pandas as pd
import re
import operator
from itertools import islice
import csv
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

df = pd.read_csv('data/athlete_events.csv', usecols=['Team', 'Medal'])

print('yo')
print(df.head())

countries = df['Team'].tolist()
medals = df['Medal'].tolist()


gold_count = dict()
silver_count = dict()
bronze_count = dict()
zero_count = dict()

for index, row in df.iterrows():
    if row['Medal'] == 'Gold':
        if row['Team'] in gold_count:
            gold_count[row['Team']] += 1
        else:
            gold_count[row['Team']] = 1

    if row['Medal'] == 'Silver':
        if row['Team'] in silver_count:
            silver_count[row['Team']] += 1
        else:
            silver_count[row['Team']] = 1

    if row['Medal'] == 'Bronze':
        if row['Team'] in bronze_count:
            bronze_count[row['Team']] += 1
        else:
            bronze_count[row['Team']] = 1

    if row['Medal'] == 0 or row['Medal'] == '0':
            zero_count[row['Team']] = 0


medal_count = dict()

for key in gold_count:
    medal_count[key] = [gold_count[key]]


for key in silver_count:
        if key in medal_count:
            medal_count[key].append(silver_count[key])
        else:
            medal_count[key] = [0, silver_count[key]]

print(medal_count)

for key in bronze_count:
        if key in medal_count:
            medal_count[key].append(bronze_count[key])
        else:
            medal_count[key] = [0, 0, bronze_count[key]]



for key in zero_count:
        if key in medal_count:
            medal_count[key].append(zero_count[key])
        else:
            medal_count[key] = [0, 0, 0, 0]

print(medal_count)


#print(gold_count)
#print(silver_count)
#print(bronze_count)

big_dict = []
for key in medal_count:
    big_dict.append({
        "Country": key,
        "Gold_Count": medal_count[key][0],
        "Silver_Count": medal_count[key][1],
        "Bronze_Count": medal_count[key][2],
        "Zero_Count": medal_count[key][3]

    })


print(big_dict)

fields = ['Country', 'Gold_Count', 'Silver_Count', 'Bronze_Count', 'Zero_Count']
#with open('country_medal_count.csv', 'w') as csvfile:
#    writer = csv.DictWriter(csvfile, fieldnames=fields)
#    writer.writeheader()
#    writer.writerows(big_dict)
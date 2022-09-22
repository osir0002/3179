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
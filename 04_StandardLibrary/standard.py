import array

import math

import random
print(random.randint(1,10))
print(random.choice(['apple','banana','orange']))


import os

print(os.getcwd)
os.mkdir('test_dir')

## high level operatons on the files and collection of files

import shutil
shutil.copy('source.txt','destination.txt')

import json

## for data serialization
data={'name':'rakesh','age':5}


converted_json= json.dumps(data) ## this concert to json

json.loads(converted_json) ## again back to dictionary


## csv
import csv
with open('example.csv',mode='w') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['rakesh',32])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)



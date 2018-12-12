# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:01:54 2018

@author: Jeroen van Renen
"""
from collections import Counter
import pandas as pd

#part one
input_codes  = 'C:/DATA/aoc_2018/2_input.txt'
with open(input_codes, 'r') as f:
    list_box_ids = (f.read().splitlines())

def find_2(box_id):
    result = (Counter(box_id).most_common())
    result_2 = [ x for x in result if x[1]==2 ]
    if result_2:
        return True
    else:
        return False

def find_3(box_id):
    result = (Counter(box_id).most_common())
    result_3 = [ x for x in result if x[1]==3 ]
    if result_3:
        return 1
    else:
        return 0

count_2 = 0
count_3 = 0
for i in list_box_ids:
    count_2 += find_2(i)
    count_3 += find_3(i)
    
print("count_2: ",count_2)
print("count_3: ",count_3)
print(count_2*count_3)


#part two
def compare_boxid(data,box_ids):
    result = 0
    for i in box_ids:
        if i == data:
            continue
        code = str()
        for x in range(len(data)):
            if data[x] == i[x]:
                code = code+data[x]
        if len(code)+1 == len(data):
            result = code
    return result

df = pd.read_csv('C:/DATA/aoc_2018/2_input.txt', sep=" ", header=None)
df.columns = ["box_id"]
box_ids = df.box_id
df['compare'] = df.box_id.apply(lambda row: compare_boxid(row,box_ids))
df = df[df.compare != 0]
print(df.compare)


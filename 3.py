# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:16:53 2018

@author: Jeroen van Renen
"""
import pandas as pd
from collections import Counter

#part one
fabric = 1000
#fabric = 8
#input_claims  = 'C:/DATA/aoc_2018/3_test.txt'
input_claims  = 'C:/DATA/aoc_2018/3_input.txt'
with open(input_claims, 'r') as f:
    list_claims = (f.read().splitlines())



claim_nr = [ int((x.split()[0]).split('#')[1]) for x in list_claims ]
coord_x = [ int((x.split()[2]).split(',')[0]) for x in list_claims ]
coord_ytop = [ int((((x.split()[2]).split(',')[1])).strip(':')) for x in list_claims ]
row_wide = [ int((x.split()[3]).split('x')[0]) for x in list_claims ]
row_tall = [ int((x.split()[3]).split('x')[1]) for x in list_claims ]

print("Total sq inches in claims needed: ", sum([ (row_wide[i]*row_tall[i]) for i in range(len(row_wide)) ]))

df = pd.DataFrame({
        'claim_nr': claim_nr,
        'coord_x': coord_x,
        'coord_ytop': coord_ytop,
        'row_wide': row_wide,
        'row_tall': row_tall
        })

def coord_x_y(x_start, y_start, row_wide, row_tall):
      result = set()
      for w in range(row_wide):
          for t in range(row_tall):
              result.add((x_start+w,y_start+t))
      return result

def get_overlap(claim_nr, row_coord, all_coord):
    for i in range(all_coord.count()):
        if (row_coord & all_coord.iloc[i]) and claim_nr-1 != i:
            return True
    return False

def get_inches(all_coord):
    result = Counter()
    for row in all_coord:
        result.update(row)
    total = [ i for i in result.values() if i > 1 ]
    return len(total)


df['coord_y'] = df.apply(lambda row: fabric-row['coord_ytop']-row['row_tall'], axis=1)
df['coord_x_y'] = df.apply(lambda row: coord_x_y(row['coord_x'],row['coord_y'],row['row_wide'],row['row_tall']), axis=1)
df['overlap'] = df.apply(lambda row: get_overlap(row['claim_nr'],row['coord_x_y'],df.coord_x_y), axis=1)
print("Total inches of overlap: ", get_inches(df.coord_x_y))
#part two
print("Claim without overlap: ", df.loc[df['overlap'] == False])
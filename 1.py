# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:37:04 2018

@author: Jeroen van Renen
"""

input_freq  = 'C:/DATA/aoc_2018/1_input.txt'
with open(input_freq, 'r') as f:
    freq_list = list(map(lambda x: (int(x)), (f.read().splitlines())))
    
#Part one
print(sum(freq_list))

#Part two
def find_freq_twice(freq_list):
    freq=0
    freq_history= set()
    loop=0
    while True:
        loop+=1
        for i in freq_list:
            freq += i
            if freq in freq_history:
                print("number of loops: ",loop)
                return freq
            else:
                freq_history.add(freq)

find_freq_twice(freq_list)
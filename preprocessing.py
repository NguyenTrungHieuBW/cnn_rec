# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:46:15 2023

@author: PC Market
"""

import csv
import json


f = open("D://caser_pytorch-master//caser_pytorch-master//Movies_and_TV_5.json", "r", encoding= 'utf-8')

listdic = f.readlines()
'''
a = []
for i in range(len(listdic)):
    a.append(json.loads(listdic[i]))
'''

a = []
for i in range(len(listdic)):
    b = []
    #Split uid
    s = listdic[i].split("reviewerID\": \"")
    s = s[1].split("\", \"asin\": \"")
    b.append(s[0])
    #Split iid
    s =  s[1].split("\", \"reviewerName\": \"")
    if(len(s)==1):
        s =  s[0].split("\", \"helpful\": ")
    b.append(s[0])
    #Split rating
    print(i)
    s =  s[1].split("overall\": ")
    s = s[1].split(", \"summary\": \"")
    b.append(s[0])
    a.append(b)
    
with open('D://caser_pytorch-master//caser_pytorch-master//datasets//review.txt', 'w') as f:
    for line in a:
        s = line[0] + " " + line[1] + " " + line[2] 
        f.write(s)
        f.write('\n')
        
    
#s = b[0] + " " + b[1] + " " + b[2] 
    
with open('Movies_and_TV_5.txt', 'w') as f:
    for line in a:
        s = line[0] + " " + line[1] + " " + line[2] 
        f.write(s)
        f.write('\n')
        
        
with open('train.txt', 'w') as f:
    for line in a[0:10000]:
        s = line[0] + " " + line[1] + " " + line[2] 
        f.write(s)
        f.write('\n')
        
with open('test.txt', 'w') as f:
    for line in a[10000:11000]:
        s = line[0] + " " + line[1] + " " + line[2] 
        f.write(s)
        f.write('\n')
        
with open('train_val.txt', 'w') as f:
    for line in a[0:9000]:
        s = line[0] + " " + line[1] + " " + line[2] 
        f.write(s)
        f.write('\n')
        
with open('test_val.txt', 'w') as f:
    for line in a[10000:11000]:
        s = line[0] + " " + line[1] + " " + line[2] 
        f.write(s)
        f.write('\n')
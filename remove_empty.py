# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:00:02 2023

@author: PC Market
"""

f = open("D://caser_pytorch-master//caser_pytorch-master//datasets//amazon3//test//train.txt", "r", encoding= 'utf-8')
train = f.readlines()

train2 = []
for i in range(len(train)):
    if(train[i]!="\n"):
        train2.append(train[i])
        
        
f = open("D://caser_pytorch-master//caser_pytorch-master//datasets//amazon3//test//test.txt", "r", encoding= 'utf-8')
test = f.readlines()

test2 = []
for i in range(len(test)):
    if(test[i]!="\n"):
        test2.append(test[i])
        
with open('D://caser_pytorch-master//caser_pytorch-master//datasets//amazon3//test//train.txt', 'w') as f:
    for line in train2:
        s = line[0] + " " + line[1] + " " + line[2]
        f.write(s)
        f.write('\n')
    
with open('D://caser_pytorch-master//caser_pytorch-master//datasets//amazon3//test//test.txt', 'w') as f:
    for line in test2:
        s = line[0] + " " + line[1] + " " + line[2]
        f.write(s)
        f.write('\n') 
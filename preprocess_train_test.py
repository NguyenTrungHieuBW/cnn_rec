# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:55:05 2023

@author: PC Market
"""
f = open("D://caser_pytorch-master//caser_pytorch-master//datasets//review.txt", "r", encoding= 'utf-8')
review = f.readlines()

reviewnp = []
for i in range(len(review)):
    reviewnp.append(review[i].split(' '))

f = open("D://caser_pytorch-master//caser_pytorch-master//preprocessed_data", "r", encoding= 'utf-8')
listdic = f.readlines()

listdic[0]
s1 = listdic[0].split('\t')

train = []
test = []
for i in range(len(listdic)):
    print(i)
    s = listdic[i].split('\t')
    b = [] 
    b.append(s[2])
    b.append(s[3])
    
    for j in range(len(reviewnp)):
        if(b[0] == reviewnp[j][0] and b[1] == reviewnp[j][1]):
            score = reviewnp[j][2]
            b.append(score)
            break
    if(s[0]=='train'):
        train.append(b)
    else:
        test.append(b)
        
        
with open('train1.txt', 'w') as f:
    for line in train:
        s = line[0] + " " + line[1] + " " + str(line[2]) 
        f.write(s)
        f.write('\n')
    
with open('test1.txt', 'w') as f:
    for line in test:
        s = line[0] + " " + line[1] + " " + str(line[2]) 
        f.write(s)
        f.write('\n') 

#get n user
f = open("Movies_and_TV_5.json", "r", encoding= 'utf-8')

listdic2 = f.readlines()

n = 500
set_user = set()

for i in range(len(listdic)):
    
    s = listdic[i].split('\t')
    set_user.add(s[2])
    if(len(set_user)==n):
        break

train = []
test = []    
for i in range(len(listdic)):
    
    print(i)
    s = listdic[i].split('\t')
    if(s[2] in set_user):
        b = [] 
        b.append(s[2])
        b.append(s[3])
        for j in range(len(reviewnp)):
            if(b[0] == reviewnp[j][0] and b[1] == reviewnp[j][1]):
                score = reviewnp[j][2]
                b.append(score)
                break
        if(s[0]=='train'):
            train.append(b)
        else:
            test.append(b)
            
for i in range(len(test)):
    if(len(test[i])==2):
        test[i].append("2.5\n")

for i in range(len(train)):
    if(len(train[i])==2):
        train[i].append("2.5\n")
        
for i in range(len(test)):
    train[i][-1].strip("/n")
        
with open('D://caser_pytorch-master//caser_pytorch-master//datasets//amazon3//test//train.txt', 'w') as f:
    for line in train:
        s = line[0] + " " + line[1] + " " + line[2]
        f.write(s)
        #f.write('\n')
    
with open('D://caser_pytorch-master//caser_pytorch-master//datasets//amazon3//test//test.txt', 'w') as f:
    for line in test:
        s = line[0] + " " + line[1] + " " + line[2]
        f.write(s)
        #f.write('\n') 

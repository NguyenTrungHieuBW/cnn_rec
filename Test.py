# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:24:50 2023

@author: PC Market
"""

f = open('datasets/amazon/test/train.txt', "r", encoding= 'utf-8')
f2 = open('datasets/ml1m/test/train.txt', "r", encoding= 'utf-8')

f11 = f.readlines()
f21 = f2.readlines()

f11[0][0]
f21[0][1]
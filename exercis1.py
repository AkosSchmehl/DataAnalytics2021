# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:40:08 2021

@author: Ákos Schméhl
"""

"Exercise 1.1"

"15 ones"

list1 = []

for x in range(15):
    list1.append(1)
    
print("15 ones")
print(list1)



"15 7s"

list2 = []

for x in range(15):
    list2.append(7)
    
print("15 7s")
print(list2)



"100 to 150"

list3 = []

for x in range(100, 151):
    list3.append(x)
    
print("100 to 150")
print(list3)



"even 100"

list4 = []

for x in range(0, 101):
    if x % 2 == 0:
        list4.append(x)
        
print("even 100")
print(list4)



"divided by 4"

list5 = []

for x in range(1950, 2021):
    if x % 4 == 0:
        list5.append(x)
        
print("divided by 4")
print(list5)

#####################################################
#####################################################

"Exercise 1.2"

import numpy as np
from numpy import random

zeroes = np.zeros(15)
print(zeroes)

ones = np.ones(15)
print(ones)

sevens=np.ones(15)*7
print(sevens)

array1 = np.arange(100, 151)
print(array1)

array2 = np.arange(1900, 2022)
print(array2)

array3 = np.arange(100, 151, 2)
print(array3)

array4 = np.arange(1952, 2021, 4)
print(array4)

#####################################################
#####################################################

"Exercise 1.3"

data1 = np.arange(1, 50).reshape(7, 7)
print(data1)

data2 = random.randint(5, size=(8, 8))
print(data2)

data3 = np.random.randn(3)
data3 = np.random.randn(8, 8)
print(data3)

#####################################################
#####################################################

"Exercise 1.4"

data4 = np.linspace(0, 1, 10)
print(data4)

data5 = np.linspace(0, 5, 100).reshape(10,10)
print(data5)

#####################################################
#####################################################
"Exercise 1.5"

list_1 = [23,34,54,34,56]
list_2 = [33,56,78,65,78]
list_3 = [41,32,11,34,56]

combined = [list_1, list_2, list_3]

matrix = np.array(combined)

array5 = np.arange(128, 256).reshape(16,8)

array6 = np.arange(0.05, 5.05, 0.05).reshape(10,10)

#####################################################
#####################################################
"Exercise 1.6"

dataset = np.arange(1, 37).reshape(6, 6)
slice = dataset[3:,2:]
column = dataset[:4,3]
row = dataset[2,:]
section = dataset[3:]

#####################################################
#####################################################
"Exercise 1.7"

dataset = np.arange(1, 37).reshape(6, 6)
total = np.sum(dataset)
total_odd= np.sum(dataset[dataset%2==1])
deviation = np.std(dataset)
sum_column= np.sum(dataset, axis=0)
sum_row= np.sum(dataset, axis=1)
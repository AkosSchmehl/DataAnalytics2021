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

#####################################################
#####################################################

"15 7s"

list2 = []

for x in range(15):
    list2.append(7)
    
print("15 7s")
print(list2)

#####################################################
#####################################################

"100 to 150"

list3 = []

for x in range(100, 151):
    list3.append(x)
    
print("100 to 150")
print(list3)

#####################################################
#####################################################

"even 100"

list4 = []

for x in range(0, 101):
    if x % 2 == 0:
        list4.append(x)
        
print("even 100")
print(list4)

#####################################################
#####################################################

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

array4 = np.arange(1950, 2021)
print(array4)
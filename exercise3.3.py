# -*- coding: utf-8 -*-



import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# we need the calendar module for this one
import calendar

# function one, this fixes the month
# luckily Python has a module called calendar
# which can convert these abbrevations to numbers
def change_month(row):
    return list(calendar.month_abbr).index(row['Month'])


# function two
# fill in the missing part of the year
def fix_year(row):
    year = int(row['Year'])
    if year > 50:
        return int(f"19{row['Year']}")
    else:
        return int(f"20{row['Year']}")



data= pd.read_csv('groceries.csv')

#replace NaN values
data['Fish'].fillna((data['Fish'].mean()), inplace=True)
data['Pork'].fillna((data['Fish'].mean()), inplace=True)
data['Sunflower-oil'].fillna((data['Fish'].mean()), inplace=True)

# before you apply the functions to year and month, we need
# to split the original date into two columns:
data[['Month', 'Year']] = data['Month'].str.split('-', 1, expand=True)

data['Month'] = data.apply(change_month, axis=1)
data['Year'] = data.apply(fix_year, axis=1)

correlation =data.corr()

plt.clf()
sns.heatmap(correlation)
plt.figure()

#Pork has the least correlation with most of the produce except for
#other types of meat and sunflower-oil but even these have low 
#correlation with it

#Most oils have high correlation with spices, legumes(such as peanuts)
#and cereals as oil is derived from these and are often used together
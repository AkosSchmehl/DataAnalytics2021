# -*- coding: utf-8 -*-



import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mpg= (sns.load_dataset('mpg'))
data= pd.read_csv('mpg.csv')

data['liters_per_100_km']=100 * 3.785411784/1.609344*data["mpg"]
data = data.drop('mpg', axis=1)
data = data.drop('name', axis=1)

data = data.drop('acceleration', axis=1)
data = data.drop('model_year', axis=1)

data = data.drop('horsepower', axis=1)
data = data.drop('displacement', axis=1)

correlations= data.corr()

#I removed the horsepower and displacement columns because as the number of cylinders 
#increases, more displacement is allowed and more fresh air  can get into a cylinder,
#the more efficient and powerful the engine will be which will typically 
#lead to more torque(in this case horsepower) and the power of the car increases.
#But all 3 of them play a big part in the actual power of the car and they are all
#related to eachother.
#link: https://www.reddit.com/r/explainlikeimfive/comments/2ws0yl/eli5_in_car_engines_whats_the_relationship/

plt.clf()
sns.pairplot(data, hue='origin')
plt.figure()

plt.clf()

sns.scatterplot(x='liters_per_100_km', y='cylinders', data=data, hue="origin")

plt.figure()

plt.clf()

#sns.scatterplot(x='weight', y='displacement', data=data, hue="origin")


plt.figure()

#USA tends to have a higher consumption
#Europe tends to have a lower consumption
#more cylinders does not necessarily mean more consumption
#around 4-5 cylinders the weight shifts to be lighter and consumption goes up
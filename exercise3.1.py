# -*- coding: utf-8 -*-



import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

penguins = (sns.load_dataset('penguins'))
data= pd.read_csv('penguins.csv')

plt.clf()

sns.pairplot(penguins)
Correlation =penguins.corr()

plt.figure()

#bigger flipper= bigger body_mass and bigger bill_length

plt.clf()

sns.pairplot(penguins, hue='island')

plt.figure()

#Torgensen has the smallest size numbers by far

penguin_amount = penguins['island'].value_counts()
penguin_species = penguins['species'].value_counts()

plt.clf()

sns.pairplot(penguins, hue='species')
plt.figure()
#minimal difference between the species and the islands plot

plt.clf()
sns.pairplot(penguins, hue='sex')
plt.figure()
#the sex column does not affect the end result that much

plt.clf()

sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', data=penguins, hue="species")
plt.figure()

plt.clf()

sns.scatterplot(x='bill_length_mm', y='flipper_length_mm', data=penguins, hue="island")
plt.figure()

#they are both the same

plt.clf()
sns.violinplot(x='species',y="flipper_length_mm", data=penguins, hue="island")
plt.figure()

plt.clf()
sns.swarmplot(x='species', y="flipper_length_mm", data=penguins, hue="island")
plt.figure()

#based on flipper_length the Adelie species is the only one that is present
#on the 3 islands and it has the smallest measurments out of the 3 species
#while the gentoo has the highest measurments 2 out of the 3 parameters

plt.clf()
sns.violinplot(x='species',y="bill_length_mm", data=penguins, hue="island")
plt.figure()

plt.clf()
sns.swarmplot(x='species', y="bill_length_mm", data=penguins, hue="island")
plt.figure()

#based on bill_length it shows the same
 
plt.clf()
sns.violinplot(x='species',y="body_mass_g", data=penguins, hue="island")
plt.figure()

plt.clf()
sns.swarmplot(x='species', y="body_mass_g", data=penguins, hue="island")
plt.figure()

#based on body_mass it shows the same
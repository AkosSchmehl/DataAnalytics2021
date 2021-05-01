# -*- coding: utf-8 -*-



import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
import json
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup 
import requests
from flatten_json import flatten

url = "https://en.wikipedia.org/wiki/Rovaniemi"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

latitude = soup.find('span' , class_='latitude').text
longitude = soup.find('span' , class_='longitude').text

nickname = soup.find('div', class_='nickname').text

population = soup.find(class_='infobox geography vcard')

print(population.prettify())
popstring = ""
btes= population.find_all('td',class_='infobox-data')
for i in btes:
    tr = i.find('tr',class_="mergedrow")
    if i.string == "63,556":
        popstring = i.string
    print (i.text.strip())
    
print ("the population of Rovaniemi " + popstring)
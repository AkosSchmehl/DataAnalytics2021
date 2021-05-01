# -*- coding: utf-8 -*-



import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar
import json
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup as bs
import requests
from flatten_json import flatten

simple_data = pd.read_json('simple.json')

# create an ElementTree object of the file
xtree = et.parse("simple.xml")
node = xtree.getroot()
 
# grab the values from the data-item in the XML
e_id = node.find("id").text
e_brand = node.find("brand").text
e_model = node.find("model").text
e_year = node.find("year").text
e_owned_by = node.find("owned_by").text
e_acquired = node.find("acquired").text
e_price = node.find("price").text
 
# data and columns for new dataframe
df_data = []
df_cols = ["id", "brand", "model", "year", "owned_by", "acquired", "price"]
 
# add actual data
row = {
       "id": e_id,
       "brand": e_brand,
       "model": e_model,
       "year": e_year,
       "owned_by": e_owned_by,
       "acquired": e_acquired,
       "price": e_price
       }
 
df_data.append(row)
 
# create DataFrame
df = pd.DataFrame(data = df_data, columns = df_cols)

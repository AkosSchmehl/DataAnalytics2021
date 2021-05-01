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

url = "https://en.wikipedia.org/wiki/List_of_countries_by_average_yearly_temperature"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data = pd.read_html(url)
actual_data = data[0]

                    
actual_data.columns = ['Country', 'avg_temp']
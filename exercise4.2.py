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

url= "https://edu.frostbit.fi/api/events/"
response= json.loads(requests.get(url).text)
events_df = pd.json_normalize(response)
# this is for cases where there is a list of data# if only one object, 
#then its just => dict_flattened= flatten(response)
dict_flattened= (flatten(record, '.') for record in response)
#events_df= pd.DataFrame(dict_flattened)
# if this crashes, comment this out
#events_df= events_df.drop('contact', axis=1)


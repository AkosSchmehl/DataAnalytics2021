# -*- coding: utf-8 -*-
"""


@author: Ákos Schméhl
"""

import numpy as np
import pandas as pd
from scipy import stats
import datetime as dt
    

pd.set_option('display.float_format', lambda x: '%.1f' % x)
purchases = pd.read_csv('purchases.csv')

purchases = purchases.drop('LPA Number', axis=1)
purchases = purchases.drop('Requisition Number', axis=1)
purchases = purchases.drop('Acquisition Type', axis=1)
purchases = purchases.drop('Acquisition Method', axis=1)
purchases = purchases.drop('Supplier Code', axis=1)
purchases = purchases.drop('Supplier Name', axis=1)
purchases = purchases.drop('Supplier Qualifications', axis=1)
purchases = purchases.drop('Supplier Zip Code', axis=1)
purchases = purchases.drop('CalCard', axis=1)
purchases = purchases.drop('Classification Codes', axis=1)
purchases = purchases.drop('Normalized UNSPSC', axis=1)
purchases = purchases.drop('Class', axis=1)
purchases = purchases.drop('Class Title', axis=1)
purchases = purchases.drop('Family', axis=1)
purchases = purchases.drop('Family Title', axis=1)
purchases = purchases.drop('Segment', axis=1)
purchases = purchases.drop('Segment Title', axis=1)
purchases = purchases.drop('Location', axis=1)


total_single=purchases[purchases["Purchase Order Number"]=="018H2015"]
total_price=np.sum(total_single["Total Price"])


name_single=purchases[purchases["Purchase Order Number"]=="3176273"]
print(name_single['Item Name'])
print(name_single["Item Description"])


PurchaseByYear = purchases[purchases['Purchase Date'].str.contains('2013')]


most_common_department = purchases['Department Name'].value_counts()[:5].index.tolist()


purchases_sorted= purchases.sort_values('Department Name')


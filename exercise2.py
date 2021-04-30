# -*- coding: utf-8 -*-
"""


@author: Ákos Schméhl
"""
import numpy as np
import pandas as pd
from scipy import stats

   
pd.set_option('display.float_format', lambda x: '%.1f' % x)

loans = pd.read_csv('loans.csv')

#loans = loans[(np.abs(stats.zscore(loans)) < 3).all(axis=1)]

#######################################################

"exercise 2.1"

loans = loans.drop('Customer ID', axis=1)
print(loans.head())



loans["Actual Annual Income"]=loans["Annual Income"] -12*loans["Monthly Debt"]

loans = loans.drop('Loan Status', axis=1)
loans = loans.drop('Credit Score', axis=1)
loans = loans.drop('Years in current job', axis=1)
loans = loans.drop('Years of Credit History', axis=1)
loans = loans.drop('Months since last delinquent', axis=1)
loans = loans.drop('Current Credit Balance', axis=1)
loans = loans.drop('Maximum Open Credit', axis=1)
loans = loans.drop('Tax Liens', axis=1)

loans_filtered=loans[loans['Current Loan Amount'] < 99999999]

loans=loans_filtered

loans = loans[loans['Annual Income'].notnull()]

average_current_loan_amount = loans['Current Loan Amount'].mean()

lowest_income=loans['Annual Income'].min() 
highest_income=loans['Annual Income'].max() 


single=loans[loans["Loan ID"]=="bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d"]
home_ownership=single.iloc[0]["Home Ownership"]


single2=loans[loans["Loan ID"]=="76fa89b9-e6a8-49af-afa1-8151315aba8e"]
actual_annual_income = single2["Actual Annual Income"]


smallest_actual_income=loans["Actual Annual Income"].min()
print(smallest_actual_income)


long_term_loans=loans[loans['Term'] == "Long Term"].count()
print(long_term_loans["Loan ID"])


bankrupt_loaners=loans[loans['Bankruptcies'] ==1].count()
print(bankrupt_loaners["Loan ID"])


home_improvements=loans[(loans["Term"]=="Short Term") & (loans["Purpose"]=="Home Improvements")].count()
print(home_improvements["Loan ID"])


unique_purpose = loans['Purpose'].unique()


most_common_loans = loans['Purpose'].value_counts()[:3].index.tolist()


correlations= loans.corr()
print("There is a correlation between Number of Credit Problems and Bankruptcies")
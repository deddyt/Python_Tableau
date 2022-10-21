#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:03:57 2022

@author: deddy
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('1.3 loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('1.3 loan_data_json.json') as json_file:
    data = json.load(json_file)
#    print(data)
    
#transform to dataframe
loandata = pd.DataFrame(data)

#find unique values for the Purpose column
loandata['purpose'].unique()
 
#describe the data
loandata.describe()

#describe the data for a specification
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp() to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#FICO score
fico = 700

# fico >= 300 and < 400: very poor
# fico >= 400 and < 600: poor
# fico >= 600 and < 660: fair
# fico >= 660 and < 780: good
# fico >= 780 : excellent

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 600 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 780:
    ficocat = 'Good'
elif fico >= 780:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown' 
print(ficocat)

#for loops
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >= 780:
            cat = 'Excellent'
        else:
            cat = 'Unknown'  
    except:
        cat = 'Error'
    
    ficocat.append(cat)

#convert ficocat from list to series
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if condition is met'

#for interest rates, create a new column if rate > 0.12 then high, else low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red', width = 0.2)
plt.show()

#scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()

#write to csv
loandata.to_csv('loan_cleaned.csv', index = True)


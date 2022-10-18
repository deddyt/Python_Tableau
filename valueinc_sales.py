#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:50:40 2022

@author: deddy
"""

import pandas as pd

data = pd.read_csv('transaction.csv', sep=';')

#Summary of data
data.info()

#Calculation
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem 
ProfitPerTransaction =  ProfitPerItem * NumberofItemPurchased

CostPerTransaction = CostPerItem * NumberofItemPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberofItemPurchased

#CostPerTransaction Column Calculation
CostPerItem = data['CostPerItem']
NumberofItemPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemPurchased

#Adding New Column to Dataframe
data['CostPerTransaction'] = CostPerTransaction

#Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost) / Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

print(data['Markup'])

#Rounding Markup
roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)

#Combine Data Fields
#my_data = data['Day']+'-'

#Check data type
print(data['Day'].dtype)

#Change column type
day = data['Day'].astype(str)
print(day.dtype)

my_date = day+'-'+data['Month']+'-'+data['Year'].astype(str)
data['date'] = my_date

#Using iloc to view specific column/row
data.iloc[0]  #view the row with index = 0
data.iloc[0:3]  #first 3 rows
data.iloc[-5:]  #last 5 rows
data.head(5)  #first 5 rows
data.iloc[:,2]  #all rows 2nd col

#Split client_keywords field
split_col = data['ClientKeywords'].str.split(',' , expand=True)

#Create new columns from split column for client keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#Using Replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#Lower function to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#Merge files, bring in new dataset
seasons = pd.read_csv('5.4 value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on = 'Month')

#Drop columns
data = data.drop('ClientKeywords', axis = 1)
data = data.drop(['Day','Month','Year'], axis = 1)

#Export into CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)



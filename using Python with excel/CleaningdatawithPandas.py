import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('Profile.csv',header=None)
df.columns = ['Items','Brand','price','earn','a','b','c']
print(df)
df.drop(columns='price',inplace=True)# remove price column

df = df.set_index('Brand')
print(df)
print(df.loc['Supreme']) #index the brand and looking for supreme brand items
print('=======================================================')
print(df.loc['Supreme':,'Items'])# print items from supreme.
# : means from supreme to the last data
print('=======================================================')
df.first = df.Items.str.split(expand=True) #splite the columns data based on space
print(df)
print('=======================================================')
#replace all NaN value by N/A strings

df = df.replace(np.nan,'N/A',regex = True)
to_excel = df.to_excel('modified.xlsx')

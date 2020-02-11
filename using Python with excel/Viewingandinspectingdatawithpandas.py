import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Profile.csv',header=None)
df.columns = ['Items','Brand','price','earn','a','b','c']

print(df.columns)
print(df['Brand'])
print(df[['Brand','a']])
print(df[['Brand','a','c']])
print('===========================================')
print(df)
print(df['a'][0:2])
print(df.iloc[0])
print(df.iloc[2,1])#looking for AJ1

wanted_values = df[['a','b']]
stored = wanted_values.to_excel('abc.xlsx',index=None)
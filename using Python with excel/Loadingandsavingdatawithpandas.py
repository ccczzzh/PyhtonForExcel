import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('Profile.csv',header=None)
df.columns = ['Items','Brand','price','earn','a','b','c']
print(df)
df.to_excel('modified.xlsx')
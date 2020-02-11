import pandas as pd

df = pd.read_csv('Profile.csv',header=None)
df.columns = ['Items','Brand','price','earn','a','b','c']
#print(df) filer
print(df.loc[df['Brand'] =='Supreme'])
print(df.loc[(df['Brand'] =='Supreme') & (df['Items'] == 'lighter')])
df['Tax %'] = df['c'].apply(lambda x:0.15 if 20<x<30 else.2 if 30<x<40 else.4)
#print(df)
# add another columns called Tax Owed
df['Tax Owed'] = df['c']*df['Tax %']
print(df['Tax Owed'])
#remove columns by column names
to_drop = ['Items','a','b','Tax %']
df.drop(columns=to_drop,inplace=True)
print(df)
# conditional
df['Test Col'] = False
df.loc[df['c'] <100,'Test Col']=True
print(df.groupby(['Test Col']).mean())
# sort
print(df.groupby(['Test Col']).mean().sort_values('c'))

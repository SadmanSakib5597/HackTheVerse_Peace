import pandas as pd
import numpy as np
import random
#using numpy's randint
x=100
y=5
df = pd.DataFrame(np.random.randint(0,100,size=(x,y)), columns=list('ABCDE'))
df['A']=np.random.randint(980,1050,size=(x,y))*0.1
df['B']=np.random.randint(40,120,size=(x,y))
df['C']=np.random.randint(60,98,size=(x,y))
df['D']=np.random.randint(60,200,size=(x,y))
df['E']=df['D']+np.random.randint(40,50)
# create a new column 
# df['AminusB'] = df['A'] - (0.1 * df['B'])
# df['names'] = 'Laura'
df.rename(columns={'A': 'temperature', 'B': 'heartbeat', 'C': 'SPO2', 'D': 'bp-lower','E': 'bp-upper'},inplace=True)
# df.head(50)
print(df)
df.to_csv('file1.csv') 

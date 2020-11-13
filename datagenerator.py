import pandas as pd
import numpy as np
import random

x=2000
y=5
df = pd.DataFrame(np.random.randint(0,100,size=(x,y)), columns=list('ABCDE'))
df['A']=np.round(np.random.randint(980,1050,size=(x,y))*0.1,2)
df['B']=np.random.randint(40,120,size=(x,y))
df['C']=np.random.randint(60,98,size=(x,y))
df['D']=np.random.randint(60,120,size=(x,y))
df['E']=df['D']+np.random.randint(40,100)

df.rename(columns={'A': 'temperature', 'B': 'heartbeat', 'C': 'SPO2', 'D': 'bp-lower','E': 'bp-upper'},inplace=True)

print(df)
df.to_csv('file1.csv') 

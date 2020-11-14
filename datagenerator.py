import pandas as pd
import numpy as np
import random

x=2000
y=6
df = pd.DataFrame(np.random.randint(0,100,size=(x,y)), columns=list('ABCDEF'))
df['A']=np.round(np.random.randint(980,1050,size=(x,y))*0.1,2)
df['B']=np.random.randint(40,120,size=(x,y))
df['C']=np.random.randint(60,98,size=(x,y))
df['D']=np.random.randint(40,120,size=(x,y))
df['E']=df['D']+np.random.randint(40,100)
df["E"] = df["E"].astype(str).astype(int)
# df['D']=np.random.randint(40,120,size=(x,y))

for i in range(x):
	if int(df['C'][i])<90:
		df['F'][i]=1
	elif float(df['A'][i])>102 or (int(df['B'][i])<60 or int(df['B'][i])>120) and (int(df['D'][i])<60 or int(df['E'][i])>130):
		df['F'][i]=1
	else:
		df['F'][i]=0

df.rename(columns={'A': 'temperature', 'B': 'heartbeat', 'C': 'SPO2', 'D': 'bp-lower','E': 'bp-upper','F': 'Danger'},inplace=True)

print(df)
df.to_csv('filenew1.csv') 

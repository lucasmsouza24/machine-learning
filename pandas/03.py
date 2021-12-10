import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('/home/lucas/dev/machine-learning/data/covid_asia_weekly_trend.csv')

print('size:', df.size)
print('len:', len(df))
print('shape:', df.shape)
print('columns:', df.columns)

import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('/home/lucas/dev/machine-learning/data/covid_asia_weekly_trend.csv')

plt.hist(df['Weekly Case % Change'])
plt.show()
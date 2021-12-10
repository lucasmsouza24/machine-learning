import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from random import randint

df = pd.read_csv('/home/lucas/dev/machine-learning/data/covid_asia_weekly_trend.csv')

countries, cases = df['Country/Other'], df['Cases in the last 7 days']

x, y = [], []

cases_list = list(cases)

while len(x) < 5:
    for i in range(len(cases_list)):
        if cases[i] == max(cases_list):
            x.append(countries[i])
            y.append(cases[i])
            cases_list.remove(cases[i])

plt.bar(x, y)
plt.show()
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from random import randint

df = pd.read_csv('/home/lucas/dev/machine-learning/data/covid_asia_weekly_trend.csv')

countries, cases = df['Country/Other'], df['Cases in the last 7 days']

x, y = [], []

used_indexes = []

# pegando randomicamente 5 valores
while len(x) < 5:
    rand_index = randint(0, len(cases))

    if rand_index not in used_indexes:
        x.append(countries[rand_index])
        y.append(cases[rand_index])
        used_indexes.append(rand_index)

plt.bar(x, y)
plt.show()
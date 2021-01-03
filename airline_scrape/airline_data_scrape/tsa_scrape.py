# -*- coding: utf-8 -*-
"""
This script scrapes daily data from the Transportation Security Administration
about the number of passengers that fly on domestic flights within the US. 
"""

import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

#Data from TSA on airline passenger flight volume year over year


url = "https://www.tsa.gov/coronavirus/passenger-throughput?page=0"

#Use a header to imitate a browser, else TSA server deines access.

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

r = requests.get(url, headers=header)

table = pd.read_html(r.text)

print("There are: ", len(table), " tables")
print("Take a look at table 0")
print(type(table[0]))

df = table[0]
df.set_index("Date", inplace=True)
#df = df.sort_index(ascending=True, axis=0)
df = df.reindex(index = df.index[::-1])
print(df.head())

for col in df.columns:
    print(col)


plt.figure()
df.plot()

plt.xlabel("Date")
plt.ylabel("Daily passengers (Millions)")
plt.xticks(rotation=45)


plt.show()



avg_margin = (np.sum(df["Total Traveler Throughput (1 Year Ago - Same Weekday)"])/len(df) - np.sum(df["Total Traveler Throughput"])/len(df))/(np.sum(df["Total Traveler Throughput (1 Year Ago - Same Weekday)"])/len(df))

print(avg_margin)

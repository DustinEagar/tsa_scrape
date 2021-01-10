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


#Use a header to imitate a browser for data scraping.

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

#Creating an empty collection dataframe
df = pd.DataFrame()

#We will iterate over pages in the dataset until we reach a page without data,
#where we will break from the while loop.

i=0
while True:      
    try:
        print(i)
        url = "https://www.tsa.gov/coronavirus/passenger-throughput?page="+str(i)
    
        r = requests.get(url, headers=header)

        table = pd.read_html(r.text)
        
        df = df.append(table[0])
        i += 1
    except ValueError:
        print("Reached end of dataset. Loaded ", i, "pages of data.")
        break
    
#Reindexing by date in ascending order, renaming columns        
df.set_index("Date", inplace=True)
df = df.reindex(index = df.index[::-1])


df.rename(columns={"Total Traveler Throughput": "Travelers", "Total Traveler Throughput (1 Year Ago - Same Weekday)": "Travelers One Year Prior"}, inplace=True)
print(df.columns)

#Creating a basic plot to show the year over year difference in air traffic.
plt.figure()
df.plot()

plt.xlabel("Date")
plt.ylabel("Daily passengers (Millions)")
plt.xticks(rotation=45)


plt.show()


#Average negative change in airline traffic from start to end of dataset.
avg_margin = (np.sum(df["Travelers One Year Prior"])/len(df) - np.sum(df["Travelers"])/len(df))/(np.sum(df["Travelers One Year Prior"])/len(df))

#variables for points in dataset
data_start = df.index[0]
data_end = df.index[-1]

#A print statement that gives the average change in air traffic volume since the start of the COVID-19 pandemic.
print("Between ", data_start, " and ", data_end, ", air traffic volume in the United States decreased by, ", np.round(100*avg_margin, 2), "percent on average.")

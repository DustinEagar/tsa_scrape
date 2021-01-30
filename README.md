# tsa_scrape
Scraping and brief analysis of airline passenger data from TSA.
Data source: https://www.tsa.gov/coronavirus/passenger-throughput

Using the requests library and Pandas, this script pulls data about domestic airline traffic volume in the United States from 
the TSA, generates a plot which illustrates the impact of COVID-19 on air travel volume, and makes some basic calculations about that impact. The TSA made this dataset available as part of its response to the COVID-19 pandemic. The dataset begins on 03/01/2020, and is updated daily.

A sample of this script's output is shown below.

![alt text](https://github.com/DustinEagar/tsa_scrape/blob/main/airline_scrape/plots/plot1.png?raw=true)

#Read and process London population data 1960 - 2015 YoY

import json
from datetime import datetime
from matplotlib import pyplot as plt

#Open file and get data
filename = 'london-population-history.json'

with open(filename) as f:
    pop_data = json.load(f)
    
#Build lists from data
years, pop = [], []
for pop_dict in pop_data:
    current_year = datetime.strptime(pop_dict['Year'], "%Y-%m-%d") 
    years.append(current_year)
    pop.append(int(pop_dict['Value']))

#Plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(years, pop, c='blue')

#Format Plot
title = 'Population of London'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Population in mio', fontsize=14)

#Show Graph
plt.show()

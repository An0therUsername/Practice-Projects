#Read and process London population data 1960 - 2020 YoY

#To-do: Refactoring, While-Looping

import json
from matplotlib import pyplot as plt

#Open file and get data
filename_k = 'Population_0-14.json'
filename_a = 'Population_15-64.json'
filename_s = 'Population_65plus.json'

with open(filename_k) as f:
    pop_data_k = json.load(f)
with open(filename_a) as f:
    pop_data_a = json.load(f)
with open(filename_s) as f:
    pop_data_s = json.load(f)

#List all available countries
def all_countries():
    #Pull countries from data and build list
    countries = []
    for country in pop_data_k:
        if country['Country Name'] not in countries:
            countries.append(country['Country Name'])
    #Format list
    for c in countries:
        print(str(c))
    
#Ask user for Country selection
print('Welcome to Population Data 3000\n' + '='*40)
country_request = input('I can give you the populations age relations of most countries. Press (l) to get a list of all available countries or just name a country.')
if country_request == 'l':
    all_countries()
    country_request = input('Name a country:')
            
#Build lists from data
years_k, years_a, years_s, pop_k, pop_a, pop_s = [], [], [], [], [], []
for pop_dict in pop_data_k:
    if pop_dict['Country Name'] == country_request:
        country = (pop_dict['Country Name'])
        years_k.append(int(pop_dict['Year']))
        pop_k.append(int(pop_dict['Value']))
    elif pop_dict['Country Name'] == country_request: #doesn't work
        error = input('Sorry Country not found. Press (l) for a list.')
        if error == 'l':
            all_countries()
            country_request = input('Name a country:') 
            #need to built function to repeat program
        else:
            print('Terminating...')
for pop_dict in pop_data_a:
    if pop_dict['Country Name'] == country_request:
        years_a.append(int(pop_dict['Year']))
        pop_a.append(int(pop_dict['Value']))
for pop_dict in pop_data_s:
    if pop_dict['Country Name'] == country_request:
        years_s.append(int(pop_dict['Year']))
        pop_s.append(int(pop_dict['Value']))

#Plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(years_k, pop_k, c='blue', label='Children')
plt.plot(years_a, pop_a, c='red', label='Adults')
plt.plot(years_s, pop_s, c='green', label ='Seniors')
plt.legend(('Children', 'Adults', 'Seniors'), loc='center')

#Format Plot
title = 'Population % of ' + str(country)
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('% of total population', fontsize=14)

#Show Graph
plt.show()

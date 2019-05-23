#Population by age group by country

#To-do: Refactoring, While-Looping

import json
import sys
from matplotlib import pyplot as plt

def all_countries():
    #Pull countries from data and build list
    countries = []
    for country in pop_data_c:
        if country['Country Name'] not in countries:
            countries.append(country['Country Name'])      
    return countries

def formatCountries(countries):
    #Format list
    for c in countries:
        print(str(c))
    
def isInList(country_request, countries):
    #Checks if requested country is available
    if country_request in countries:
        return True
            
def buildLists(pop_data_c, pop_data_a, pop_data_s, country_request):      
    #Build lists from data
    years_c, years_a, years_s, pop_c, pop_a, pop_s = [], [], [], [], [], []
    for pop_dict in pop_data_c:
        if pop_dict['Country Name'] == country_request:
            country = (pop_dict['Country Name'])
            years_c.append(int(pop_dict['Year']))
            pop_c.append(int(pop_dict['Value']))
    for pop_dict in pop_data_a:
        if pop_dict['Country Name'] == country_request:
            years_a.append(int(pop_dict['Year']))
            pop_a.append(int(pop_dict['Value']))
    for pop_dict in pop_data_s:
        if pop_dict['Country Name'] == country_request:
            years_s.append(int(pop_dict['Year']))
            pop_s.append(int(pop_dict['Value']))   
    return years_c, years_a, years_s, pop_c, pop_a, pop_s, country

def plotData(years_c, years_a, years_s, pop_c, pop_a, pop_s, country):
    #Plot data
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(years_c, pop_c, c='blue', label='Children')
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


#Main Program Loop

#Open file and get data
filename_c = 'Population_0-14.json'
filename_a = 'Population_15-64.json'
filename_s = 'Population_65plus.json'

with open(filename_c) as f:
    pop_data_c = json.load(f)
with open(filename_a) as f:
    pop_data_a = json.load(f)
with open(filename_s) as f:
    pop_data_s = json.load(f)

countries = all_countries()

#Ask user for Country selection
print('Welcome to Population Data 3000\n' + '='*40)
print('I can give you the populations age relations of most countries. Press (l) to get a list of all available countries or type (quit) to exit the program.')

while True:
    country_request = input('Please select a country: ')
    if country_request in ('quit', 'q'):
        sys.exit()
    elif country_request == 'l':
        formatCountries(all_countries())
        continue
    elif country_request not in countries:        
        print("'%s' is not available. To see all available countries press (l)" %(country_request))
        if input().lower().startswith('l'):
            formatCountries(all_countries())
        continue
    else:
        years_c, years_a, years_s, pop_c, pop_a, pop_s, country = buildLists(pop_data_c, pop_data_a, pop_data_s, country_request)
        plotData(years_c, years_a, years_s, pop_c, pop_a, pop_s, country)
    
    
        
    
    
        
        

         
         


# imports
from bs4 import BeautifulSoup
import requests
import pandas as pd

# getting data
start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
data = requests.get(start_url)

# initialising soup
soup = BeautifulSoup(data.text,'html.parser')

# finding all tables
table1 = soup.find_all('table')

# for loop in tables 4th row
temp_list= []
table_rows = table1[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

# creating empty lists
star_names = []
distance =[]
mass = []
radius =[]

# appending data from the list created
for i in range(1,len(temp_list)):
    
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

# creating a dataframe
df = pd.DataFrame(list(zip(star_names,distance,mass,radius,)),columns=['star_name','distance','mass','radius'])

# saving the df as csv file
df.to_csv('brown_dwarf.csv')
print("success")
import requests
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

tickerslist = []

res = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

content = res.text

soup = BeautifulSoup(content, 'html.parser')

specific_part = soup.find(id='constituents')

rows = specific_part.find_all('tr')[1:]

for row in rows:
    data_cells = row.find_all('td')
    ticker = data_cells[0]
    for i in ticker:
        processedticker = i.text.strip()
        tickerslist.append(processedticker)

tickerslist = [i for i in tickerslist if i != '']
print(tickerslist)
input("Press Enter to exit...")


    

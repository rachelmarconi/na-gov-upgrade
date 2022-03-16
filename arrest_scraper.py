import csv
from csv import reader
import requests
from bs4 import BeautifulSoup
from datetime import date
from pathlib import Path
import pandas as pd


#YEAR = '2021'
YEAR = str(date.today().year)

url = 'https://www.umpd.umd.edu/stats/arrest_report.cfm?year='+YEAR
response = requests.get(url, headers={'User-Agent': 'Rachel Logan'}) 
html = response.content 

soup = BeautifulSoup(html, features="html.parser")
#print(soup.prettify())

table = soup.find('table').find_all('tr')

row_list = []
cell_list = []

for row_index in range(0,len(table)):
	#print(table[row_index],'\n')
	if (not row_index): 
		header_row = [cell.text.strip() for cell in table[0].find_all('th')]
		header_row.append('DESCRIPTION')
		#print(header_row)
		row_list.append(header_row)
	elif (row_index % 2):
		cell_list = [cell.text.strip() for cell in table[row_index].find_all('td')]
	else:
		cell_list.append(table[row_index].find('td').text.strip())
		row_list.append(cell_list)
		cell_list = []

path = Path('./data/all-police-arrests.csv')

if not path.is_file():
    outfile = open(path,"w",newline="")
    writer = csv.writer(outfile)
    writer.writerows(row_list)

else:
    with open(path, 'r') as prev_data_stream:
        csv_reader = reader(prev_data_stream)
        prev_data = list(csv_reader)
    
    all_data = prev_data + row_list
    pd_all_data = pd.DataFrame(all_data).drop_duplicates(keep = 'first')
    pd_all_data.to_csv(path, index = False, index_label = False, header = False)


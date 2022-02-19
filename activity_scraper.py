import csv
import requests
from bs4 import BeautifulSoup

#Can loop through, append these to download larger sets
MONTH = '2'
YEAR = '2022'

url = 'https://www.umpd.umd.edu/stats/incident_logs.cfm?year=' + YEAR + '&month=' + MONTH
#url = 'https://www.umpd.umd.edu/stats/incident_logs.cfm?year=2022&month=2
response = requests.get(url, headers={'User-Agent': 'Rachel Logan'}) 
html = response.content 

soup = BeautifulSoup(html, features="html.parser")
#print(soup.prettify())
#print(soup.find('table').find_all('tr'))

table = soup.find('table').find_all('tr')

row_list = []
cell_list = []

for row_index in range(0,len(table)):
	#print(table[row_index],'\n')
	if (not row_index): 
		#there is the issue of removing <br> leaves no space-- 
		#could replace <br> with ' ' before pulling text, but not as clean
		header_row = [cell.text.strip() for cell in table[0].find_all('th')]
		header_row.append('LOCATION')
		#print(header_row)
		row_list.append(header_row)
	elif (row_index % 2):
		cell_list = [cell.text.strip() for cell in table[row_index].find_all('td')]
	else:
		cell_list.append(table[row_index].find('td').text.strip())
		row_list.append(cell_list)
		# for cell in cell_list: 
		# 	print(cell,'\n')
		# print('-----------')
		cell_list = []
        
#should split data and time for report and incident

out_url = './data/scraped-umd-police-activity-log-'+MONTH+ '-' +YEAR+'.csv'
outfile = open(out_url,"w",newline="")
writer = csv.writer(outfile)
writer.writerows(row_list)
import csv
import requests
from bs4 import BeautifulSoup

#What to scrape?
#Could add lines to a csv at each scrape-- so data should be one row: a whole bunch of details for one item.
#The soup du jour is COVID data, but I did a lot of that in Annapolis and most things are built out now-- 
#unless I could make a map of who has tests available where. But that data isn't all in one place,
#so it doesn't give itself to a scraping exercise. 

#library catalogs? train schedules? What do we care about? concert/conference schedules?

#Coming back to the police log idea! 
#https://www.umpd.umd.edu/stats/incident_logs.cfm?year=2022&month=2
#notice the query for month and year in the URL! 

#Right now, data is in a tabular format, but there's no way to sort or even view more
#than on month at a time. How can we know what's happening most, 
#or any kind of statistics about the issues, until the yearly report?

#The data: we have case number (a UID!), the data/time and location
#(annoyingly in the same cell), the report date and time, the type of crime,
#and the disposition-- some of which is in unexplained abbreviations.

#There is a City Protect profile where you can be notified of 
#the latest incident, but that's not the same thing as an accessible database.

#There is also an arrest log!! 
#https://www.umpd.umd.edu/stats/arrest_report.cfm?year=2022
#further note the year in the url
#data includes arrest number (UID), time/data, connected case number 
#(which totally means these could be connected databases but aren't), 
#plus the age, race, and gender of the arrested individual-- 
#plus a description, which is not in correct tabular format,
#and also the crime type, also not in format.

#The arrest log is a lot more helpful for this assignment because
#it has a human-legible description and is more high-caliber info.
#It's more interesting for the reader and easier to discern 
#possible stories for reporters.

#LET'S GET DOWN TO BUSINESS

YEAR = '21'
#YEAR = '22'

url = 'https://www.umpd.umd.edu/stats/arrest_report.cfm?year=20'+YEAR
response = requests.get(url, headers={'User-Agent': 'Rachel Logan'}) 
html = response.content 

soup = BeautifulSoup(html, features="html.parser")
#print(soup.prettify())

#I got blocked??? wow-- "dotDefender blocked your request!"
#changed from User-Agent Mozilla to my name, problem gone
#only one table

table = soup.find('table').find_all('tr')

#ok, the problem here (not a big problem) is that the data alternates with
#an internal row for the description. so we take two at a time.

row_list = []
cell_list = []

for row_index in range(0,len(table)):
	#print(table[row_index],'\n')
	if (not row_index): 
		#there is the issue of removing <br> leaves no space-- 
		#could replace <br> with ' ' before pulling text, but not as clean
		header_row = [cell.text.strip() for cell in table[0].find_all('th')]
		header_row.append('DESCRIPTION')
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

out_url = './scraped-umd-police-arrest-log-'+YEAR+'.csv'
outfile = open(out_url,"w",newline="")
writer = csv.writer(outfile)
writer.writerows(row_list)
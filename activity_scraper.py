import csv
from csv import reader
import requests
from bs4 import BeautifulSoup
from datetime import date
from pathlib import Path
import pandas as pd


row_list = []
cell_list = []
header_row = []

THIS_MONTH = str(date.today().month)
THIS_YEAR = date.today().year

first = True

for YEAR in range(THIS_YEAR -1,THIS_YEAR +1):
    YEAR = str(YEAR)
    for MONTH in range(1,13):
        MONTH = str(MONTH)
        

        url = 'https://www.umpd.umd.edu/stats/incident_logs.cfm?year=' + YEAR + '&month=' + MONTH
        #url = 'https://www.umpd.umd.edu/stats/incident_logs.cfm?year=2022&month=2
        response = requests.get(url, headers={'User-Agent': 'Rachel Logan'}) 
        html = response.content 

        soup = BeautifulSoup(html, features="html.parser")
        #print(soup.prettify())
        #print(soup.find('table').find_all('tr'))

        table = soup.find('table').find_all('tr')

        for row_index in range(0,len(table)):
            #print(table[row_index],'\n')
            if (first): 
                first = False
                #there is the issue of removing <br> leaves no space-- 
                #could replace <br> with ' ' before pulling text, but not as clean
                header_row = [cell.text.strip() for cell in table[0].find_all('th')]
                header_row.append('LOCATION')
                #print(header_row)
                row_list.append(header_row)
            elif (row_index % 2):
                cell_list = [cell.text.strip() for cell in table[row_index].find_all('td')]
            elif row_index:
                cell_list.append(table[row_index].find('td').text.strip())
                row_list.append(cell_list)
                # for cell in cell_list: 
                # 	print(cell,'\n')
                # print('-----------')
                cell_list = []
                
        #should split data and time for report and incident

path = Path('./data/all-police-activity.csv')

if not path.is_file():
    outfile = open(path,"w",newline="")
    writer = csv.writer(outfile)
    writer.writerows(row_list)

else:
    with open(path, 'r') as prev_data_stream:
        csv_reader = reader(prev_data_stream)
        prev_data = list(csv_reader)
    
    everything = pd.DataFrame(row_list + prev_data)
    
    pd_all_data = everything.drop_duplicates(subset=0,keep = 'first')
    pd_all_data.to_csv(path, index = False, index_label = False, header = False)
    
    open_cases = pd.DataFrame(everything.loc[everything[4] != "CBE"])
    print("open cases\n",open_cases)
    case_filter = open_cases.duplicated(subset = 0, keep = 'last')
    rescrape_only_filter = open_cases.duplicated(keep = 'last')
    update_filter = [ (tup[0] and not tup[1]) for tup in zip(case_filter,rescrape_only_filter)]
    #[case_filter[i] and not(rescrape_only_filter[i]) for i in range(len(case_filter))]
    print("update_filter\n",update_filter)
    
    
    new_all_data = everything.loc[everything.duplicated(subset = 0, keep = False) == False]
    new_now_data = pd.DataFrame()
    for row in new_all_data.itertuples():
        year = row[2].split('/')[2].split()[0]
        if len(year)== 4 and int(year) >= (THIS_YEAR - 1):
            new_now_data.append( row , ignore_index = False)
        elif len(year)== 2 and int(year) >= (THIS_YEAR - 2001):
            new_now_data.append( row , ignore_index = False)
    
    if len(new_now_data) > 0:
        new_now_data.to_csv('./data/new_cases.csv', index = False, header = False)
    else:
        pd.DataFrame().to_csv('./data/new_cases.csv',index = False, header = False)
    print("new cases: ",new_now_data)
    
    dupes = pd.DataFrame(open_cases).loc[update_filter]
    print("dupes\n",dupes)
    #open_cases & open_cases.duplicated(subset = 0, keep = 'first')
    
    if len(dupes) > 0:
        dupe_path = ('./data/updated-activities.csv')
        dupes.to_csv(dupe_path, index = False, header = False)
    else:
        pd.DataFrame().to_csv('./data/updated-activities.csv',index = False, header = False)
    

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.zrankings.com/articles/best-ski-resorts-us"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
table = soup.find('table', class_ = 'index-table-2017')

# Defining of the dataframe
df = pd.DataFrame()

# Collecting Ddata
all_data = []
for tbody in table.find_all('tbody', class_ = 'single-resort-cell'):
    for row in tbody.find_all('tr', class_ = 'top-rowdy'):    
        # Find all data for each column
        columns = row.find_all('td')
        row_info = []
        for column in columns:
            img_link = column.find_all('a')
            if img_link:
                img = img_link[0].find_all('img')
                if img:
                    img = img[0]
                    link = img['src']
                    if 'ikon' in link.lower():
                        pass_type = 'Ikon'
                    elif 'epic' in link.lower():
                        pass_type = 'Epic'
                    elif 'collective' in link.lower():
                        pass_type = 'Mountain Collective'
                    else:
                        pass_type = "Other/None"
                    row_info.append(pass_type)                    
            else:
                row_info.append(column.text.strip())
        

        all_data.append(row_info)


pd.DataFrame(all_data).to_csv('test.csv', index=False)


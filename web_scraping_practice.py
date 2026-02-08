from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {
    "User-Agent": "BeginnerPythonProject/1.0 (your_email@example.com)"
}
page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.text, features='html.parser')

tables = soup.find_all('table', class_="wikitable sortable")
table = tables [0]

world_titles = table.find_all('th')

world_table_titles = [titles.text.strip('\n') for titles in world_titles]

print (world_table_titles)

import pandas as pd 

df = pd.DataFrame (columns = world_table_titles)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip('\n') for data in row_data]

    length = len (df)
    df.loc[length] = individual_row_data

df.to_csv (r'/workspaces/Beginner-projects/table.csv', index = False)
from bs4 import BeautifulSoup
import json

with open('info_response.html', encoding='utf-8') as fp:
    src = fp.read()

soup = BeautifulSoup(src, 'lxml')
table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')

find_all_in_table = soup.find('table', {'id': "versionsTable"}).find('tbody').find('tr')

data = {}


def find_version(tag,number):
    versionColumn = tag.find('td', {'class': 'versionColumn'}).text.strip()
    dateColumn = tag.find('td', {'class': 'dateColumn'}).text.strip()
    previousVersionsColumn = []
    g = tag.find('td', {'class': 'previousVersionsColumn'}).text.strip().split(sep=',')
    for i in g:
        previousVersionsColumn.append(i.strip())
    minVersionsColumn = tag.find('td', {'class': 'previousVersionsColumn'}).text.strip()
    data[number] = {versionColumn:{
        "dateColumn": dateColumn,
        'previousVersionsColumn': previousVersionsColumn,
        'minVersionsColumn': minVersionsColumn
    }}

    return tag.find_next_sibling()


for i in range(40):
    find_all_in_table = find_version(find_all_in_table,i)

with open("lf.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

from bs4 import BeautifulSoup
import json


def create_dict(**qwargs):
    d = {k: v for k, v in qwargs.items()}
    return d


with open('info_response.html', encoding='utf-8') as fp:
    src = fp.read()

soup = BeautifulSoup(src, 'lxml')
table = soup.find('table', {'id': "versionsTable"}).find('tbody').find_all('tr')



find_all_in_table = soup.find('table', {'id': "versionsTable"}).find('tbody').find('tr')

data = {}


def find_version(tag):

    fk = tag.find_next_sibling()
    versionColumn = fk.find('td', {'class': 'versionColumn'}).text.strip()
    dateColumn = fk.find('td', {'class': 'dateColumn'}).text.strip()
    previousVersionsColumn = fk.find('td', {'class': 'previousVersionsColumn'}).text.strip().split()
    minVersionsColumn = fk.find('td', {'class': 'previousVersionsColumn'}).text.strip()
    data[versionColumn] = {
        "dateColumn": dateColumn,
        'previousVersionsColumn': previousVersionsColumn,
        'minVersionsColumn': minVersionsColumn
       }

    return fk


for i in range(20):
    find_all_in_table = find_version(find_all_in_table)

with open("lf.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

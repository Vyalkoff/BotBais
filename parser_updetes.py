from bs4 import BeautifulSoup


with open('info_response.html',encoding='utf-8') as fp:
    src = fp.read()

soup = BeautifulSoup(src,'lxml')

find_all_in_table = soup.find('table',{'id':"versionsTable"}).find('tbody').find_all('tr')

js = dict
# print(find_all_in_table)
for item in find_all_in_table:
    print(item)
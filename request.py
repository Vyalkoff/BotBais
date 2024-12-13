import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0'}

login = "dev1c@hqss.kz"
password = "1Cdev1c@hqss.kz"

# URL для авторизации
url_login = "https://login.1c.ru/login?service=https%3A%2F%2Fportal.1c.ru%2Fpublic%2Fsecurity_check"

session = requests.Session()

response = session.get(url_login)

# Парсим страницу, чтобы извлечь необходимые скрытые параметры (например, CSRF-токены)
soup = BeautifulSoup(response.text, "html.parser")

# Пример получения скрытых полей
# Возможно, на странице есть скрытые поля (например, csrf токен)
# Проверим их на наличие и извлечем значения
hidden_inputs = soup.find_all("input", type="hidden")
data = {}
for input_tag in hidden_inputs:
    data[input_tag.get("name")] = input_tag.get("value")

# Шаг 2: Подготавливаем данные для отправки формы
data['username'] = login
data['password'] = password

# Шаг 3: Отправляем POST-запрос с логином и паролем
response_login = session.post(url_login, headers=header, data=data)
with open("response_login.html", "w", encoding="utf-8") as f:
    f.write(response_login.text)
# Проверяем, успешна ли авторизация
# if "" in response_login.text:  # Это условие зависит от структуры страницы
#     print("Ошибка авторизации")
# else:
#     print("Авторизация успешна!")

response_updates = session.get('https://releases.1c.ru/project/AccountingKz30?allUpdates=true#updates', headers=header)
with open('info_response.html', 'w', encoding='utf-8') as f:
    f.write(response_updates.text)

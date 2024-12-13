import json
import pprint

with open("lf.json", encoding="utf-8") as file:
    data = json.load(file)


def search_count_version(vers: str):
    len_data = len(data) - 1

    for number in range(len_data):
        for key, value in data[str(number)].items():
            if vers in value['previousVersionsColumn']:
                return key


def last_version(vers: dict):
    for i in data.get('0'):
        return i


last_version = last_version(data)
counter = 0
version = "3.0.50.1"
all_version = []
while last_version != version:
    version = search_count_version(version)
    all_version.append(version)
    counter += 1

print(f'С версии 3.0.50.1 До последней версии {counter}')
print(f'Релизы {'! '.join(all_version)}')

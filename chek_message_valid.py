import json
import re


def valid(message_text):
    pattern = re.compile(r'')
    with open("lf.json", encoding="utf-8") as file:
        data = json.load(file)
    len_data = len(data) - 1

    for number in range(len_data):
        for key in data[str(number)].keys():
            if key == message_text:
                return True


if __name__ == '__main__':
    valid("3.0.50.1")

import csv
from datetime import datetime

import requests


class STATUSNOTVALIDEXCEPTION(Exception):
    pass


def send_birthday_email(user: list) -> None:
    url: str = 'https://still-river-07029.herokuapp.com/'

    payload: dict = {
        "to": user[3],
        "from": "amazing-candidate@hotmail.com",
        "subject": "Happy Birthday!",
        "body": "Wishing you a happy day"}

    response = requests.post(url, json=payload)

    if response.status_code != 202:
        raise STATUSNOTVALIDEXCEPTION


def get_birthday_users(file):
    result: list = []
    datetime_format = '%Y/%m/%d'
    with open('file.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] != 'last_name' and datetime.strptime(row[2],
                                                           datetime_format).month == datetime.now().month and datetime.strptime(
                    row[2], datetime_format).day == datetime.now().day:
                result.append(row)
    return result


def main() -> None:
    list_birthday_users = get_birthday_users('file.csv')

    for user in list_birthday_users:
        try:
            send_birthday_email(user)
        except STATUSNOTVALIDEXCEPTION as error:
            print('could not send a message!')


if __name__ == '__main__':
    main()

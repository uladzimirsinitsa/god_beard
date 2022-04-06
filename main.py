"""Urls Scanner. """
import os
import random
import winsound

from string import ascii_lowercase
from string import digits

import requests

from deta import Deta
from dotenv import load_dotenv

load_dotenv()


DOMAIN = os.environ['DOMAIN']
LENGTH = os.environ['LENGTH']
PROJECT_KEY = os.environ['PROJECT_KEY']

database = Deta(PROJECT_KEY)
responses200_db = database.Base('responses200_db')


def create_string_letters_numbers() -> str:
    """Create random string. """
    possible_symbols = digits + ascii_lowercase
    return ''.join(random.choice(possible_symbols) for _ in range(int(LENGTH)))


def create_url(string_letters_numbers: str) -> str:
    """Concatanate domain and string. """
    return f'{DOMAIN}{string_letters_numbers}.jpg'


def create_record_database(url: str, string_letters_numbers: str) -> None:
    """Create record in database. """
    responses200_db.insert({
        'url': url
    }, key=string_letters_numbers)


def sent_request(url: str, string_letters_numbers: str) -> int:
    """Sent request and validation resxponse. """
    response = requests.get(url)
    if response.status_code == 200:
        winsound.Beep(370, 2000)
        create_record_database(url, string_letters_numbers)
    return response.status_code


def main():
    """Infinite cycle Script. """
    while True:
        string_letters_numbers = create_string_letters_numbers()
        url = create_url(string_letters_numbers)
        print(url, sent_request(url, string_letters_numbers))

    
if __name__ == '__main__':
    main()

"""Urls Scanner. """
import os
import secrets

from string import digits

import requests

from deta import Deta
from dotenv import load_dotenv

load_dotenv()


DOMAIN = os.environ['DOMAIN']
LENGTH = os.environ['LENGTH']
PROJECT_KEY = os.environ['PROJECT_KEY']

database = Deta(PROJECT_KEY)
responses200_db = database.Base('responses404_db')


def create_string_letters_numbers() -> str:
    """Create random string. """
    possible_symbols = f'{digits}abcdef'
    return ''.join(secrets.choice(possible_symbols) for _ in range(int(LENGTH)))


def create_url(string_letters_numbers: str) -> str:
    """Concatanate domain and string. """
    return f'{DOMAIN}{string_letters_numbers}.jpg'


def create_record_database(url: str, string_letters_numbers: str) -> None:
    """Create record in database. """
    responses200_db.insert({
        'url': url
    }, key=string_letters_numbers)


def sent_request(url: str, string_letters_numbers: str) -> None:
    """Sent request and validation resxponse. """
    response = requests.get(url)
    if response.status_code == 200:
        create_record_database(url, string_letters_numbers)


def main():
    """Infinite cycle Script. """
    while True:
        try:
            string_letters_numbers = create_string_letters_numbers()
            url = create_url(string_letters_numbers)
            sent_request(url, string_letters_numbers)
        except Exception:
            continue

    
if __name__ == '__main__':
    main()

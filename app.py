from re import compile
from bs4 import BeautifulSoup
from socket import gethostbyname

from requests import get
from requests.exceptions import RequestException

if __name__ == '__main__':
    try:
        response = get('https://sstmk.ru')
    except RequestException as e:
        raise SystemExit(e)

    host = gethostbyname('sstmk.ru')
    print(f"The sstmk.ru site is working with code = {response.status_code}. Host ip address = {host}")
    phones_urls = BeautifulSoup(response.text, 'lxml').select('a[href^="tel:"]')
    pattern = compile(r'(?:\+[\d]{1,3}?|[\d]{,3}?)\([\d]{1,}\)[\d]{1,}(?:-\d{1,}){2}')

    for phone_url in phones_urls:
        if phone_url.string:
            phone = ''.join(phone_url.string.split())

            if pattern.fullmatch(phone):
                print(f'{phone} is valid')
            else:
                print(f'{phone} is not valid')

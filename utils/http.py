import unicodedata, requests
import requests.packages.urllib3
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def get_page(url):
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
    request = requests.get(url, headers=headers)
    html = unicodedata\
        .normalize('NFKD', request.text)\
        .encode('ascii','ignore')\
        .replace('\n', ' ')
    assert request.status_code == 200, 'request error'
    try:
        return BeautifulSoup(html, 'lxml')
    except:
        import ipdb; ipdb.set_trace()
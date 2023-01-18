from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def get_page(url):
    response = urlopen(Request(url))
    soup = BeautifulSoup(response, 
                         'html.parser', 
                         from_encoding=response.info().get_param('charset'))
    
    return str(soup)

def get_robots_txt(url: str):
    if url.endswith('/'):
        path = url + 'robots.txt'
    else:
        path = url + '/robots.txt'

    robots_txt = get_page(path)
    return robots_txt




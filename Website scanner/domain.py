from urllib.parse import urlparse


def get_domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

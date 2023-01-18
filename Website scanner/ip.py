import socket


def get_ip(url):
    ip_addres = socket.gethostbyname(url)
    return ip_addres


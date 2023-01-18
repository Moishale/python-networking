import os


def get_nmap(options, ip):
    command = f'nmap {options} {ip}'
    results = os.popen(command)
    return results.read()
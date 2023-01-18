import os


def get_whois(url):
    command = f'whois {url}'
    command_output = os.popen(command)
    return command_output.read()

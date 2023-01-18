from robots_txt import *
from general import *
from domain import *
from whois import *
from nmap import *
from ip import *

MAIN_DIR = 'scans'
create_project_dir(MAIN_DIR)

def gather_info(name, url):
    domain_name = get_domain(url)
    ip_address = get_ip(domain_name)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    save_info(name, url, domain_name, whois, robots_txt, nmap)

def save_info(name, full_url, domain_name, whois, robots_txt, nmap):
    project_dir = f'{MAIN_DIR}/{name}'
    create_project_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/whois.txt', whois)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/nmap.txt', nmap)

gather_info('insta', 'https://www.instagram.com/')
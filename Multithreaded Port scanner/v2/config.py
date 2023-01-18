import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Moishales Port Scanner')
    parser.add_argument('-T', '--target', action='store', type=str, required=True,  help='ip to scan')
    parser.add_argument('-R', '--range', action='store', default=100,  type=int, required=False,  help='range of ports 1-60,000')

    return parser.parse_args()

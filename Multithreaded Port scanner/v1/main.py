import threading
import logging
import socket
import queue


TARGET = socket.gethostbyname(socket.gethostname())
NUMBER_OF_THREADS = 16
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
QUEUE = queue.Queue()


def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, port))
        return True

    except:
        return False


def scan(port):
    if port_scanner(port):
        logging.info(f'Port {port} is open')

    else:
        logging.info(f'Port {port} is closed')


def fill_queue(port_amount):
    for port in range(port_amount):
        QUEUE.put(port)

    QUEUE.join()


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        port = QUEUE.get()
        scan(port)
        QUEUE.task_done()


def run():
    if QUEUE.empty() is False:
        work()
    else:
        quit()


logging.basicConfig(format=LOG_FORMAT, level=logging.INFO,
                    datefmt='%H:%M:%S')


create_workers()
fill_queue(100)
run()
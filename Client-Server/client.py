import threading
import socket


HOST = '192.168.1.115'
PORT = 9090

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nickname = input('Nickname:')


def send():
    while True:
        try:
            message = input()
            client.send(f'{nickname}: {message}'.encode('ascii'))
        except:
            client.close()
            break


def recive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'nick:':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            client.close()
            break


message_thread = threading.Thread(target=send)
message_thread.start()

recive_thread = threading.Thread(target=recive)
recive_thread.start()

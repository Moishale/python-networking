import threading
import socket
import time
import logging
import json

HOST = '192.168.1.115'
PORT = 9090


class Server:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.clients = []
        self.nicknames = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen(3)
        print('Server is listening.....')

    def broadcast(self, message, author):
        for client in self.clients:
            if client != author:
                client.send(message.encode('ascii'))

    def handle(self, client):
        while True:
            try:
                message = client.recv(1024).decode('ascii')
                self.broadcast(message, client)
            except:
                self.clients.remove(client)
                self.nicknames.remove(
                    self.nicknames[self.clients.index(client)])
                self.broadcast(
                    f'{self.nicknames[self.clients.index(client)]} left the chat', client)
                self.close()
                break

    def start(self):
        while True:
            client, address = self.server.accept()
            print(f'{address} has connected')

            client.send('nick:'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')

            self.clients.append(client)
            self.nicknames.append(nickname)
            print(f'nickname of the client is {nickname}')

            
            self.broadcast(f'{nickname} Connected to the server!', client)

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()


server = Server()
server.start()

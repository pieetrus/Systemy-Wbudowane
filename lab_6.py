'''
Laboratorium 6 (kalkulator po telnet)
Na podstawie kalkulatora RPN opracuj serwer dostępny dla jednego użytkownika zapewniający dostęp przez protokół telnet na wybranym porcie.
'''
import socket
import time

HEADERSIZE = 10
HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    

    msg = bytes(f'{len(msg):<{HEADERSIZE}}' + msg , 'utf-8')

    clientsocket.send(msg)

    while True:
        data = clientsocket.recv(512)
        print(str(data))





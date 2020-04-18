'''
Laboratorium 6 (kalkulator po telnet)
Na podstawie kalkulatora RPN opracuj serwer dostępny dla jednego użytkownika zapewniający dostęp przez protokół telnet na wybranym porcie.
'''
import socket

HEADERSIZE = 10
HOST = '127.0.0.1'
PORT = 9990
ENTER = b'\r\n'
SPACE = b' '
BACKSPACE = b'\x08'

import operator

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv
       }




def byte_encode(stack):
    exp = ''
    for i in stack:
        exp += str(i) + ' '
    exp += '\n\r'
    return exp.encode('utf-8')


def is_not_special_char(character):
    if character == SPACE:
        return False
    if character == BACKSPACE:
        return False
    return True



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

def calculate(tokens, stack):
    for token in tokens:
        if set(token).issubset(set("0123456789.")):
            stack.append(float(token))
        elif token in ops:
            if len(stack) < 2:
                msg = 'Must have at least two parameters to perform operation'
                clientsocket.send(msg.encode('utf-8'))
                raise ValueError(msg)
            a = stack.pop()
            b = stack.pop()
            op = ops[token]
            stack.append(op(b, a))
        else:
            msg = 'Incorrect input!'
            clientsocket.send(msg.encode('utf-8'))
            raise ValueError(msg)
    return stack


while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "-----------------------------------------\n\r"
    msg += "Welcome to RPN calculator!\n\r"
    msg += "q - to exit \n\r"
    msg += "clear - to clear stack\n\r"
    msg += "-----------------------------------------\n\r"

    msg = bytes(msg, 'utf-8')

    clientsocket.send(msg)

    while True:
            stack = []
            numbers = []
            expression = ''
            while True:
                data = clientsocket.recv(512)
                while data != ENTER:
                    decoded = data.decode()
                    if len(decoded) > 0:
                        numbers.append(decoded)
                    temp = clientsocket.recv(512)
                    if temp == BACKSPACE:
                        if len(numbers) > 0:
                            numbers.pop()
                        data = b''
                        continue
                    if temp == SPACE:
                        continue
                    data = temp
                for i in numbers:
                    expression += i
                if expression == 'q':
                    exit()
                elif expression == 'clear':
                    stack = []
                    expression = ''
                    numbers = []
                    continue
                elif len(expression) == 0:
                    continue
                stack = calculate(expression.split(), stack)
                print(str(stack))
                clientsocket.send(byte_encode(stack))
                expression = ''
                numbers = []


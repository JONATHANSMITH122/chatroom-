import socket

import sys

import time

new_socket = socket.socket()

host_name = socket.gethostname()

s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))

print( "binding successful!”)

print("this is your ip: ", s_ip)

conn, add= new_socket.accept()

print("received connection from ", add[0])

print('connection established. connected from: ',add[0])

client = (conn.recv(1024)).decode()

print(client + ' has connected.')

conn.send(name.encode())

while true:

    message = input('me : ')

    conn.send(message.encode())

    message = conn.recv(1024)

    message = message.decode()

    print(client, ':', message)

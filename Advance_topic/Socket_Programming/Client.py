import socket

client_socket = socket.socket()  # creating socket for client

# it will take two argument one is ip address and second is port number that you want to connect
client_socket.connect(('localhost', 9999))
print("Creating connection..")

name = input("Enter your name: ")  # you can also send an name
client_socket.send(bytes(name, 'utf-8'))

print(client_socket.recv(1024).decode())  # it will have buffer size

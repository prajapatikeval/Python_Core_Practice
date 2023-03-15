import socket

server_socket = socket.socket()  # by default it will use tcp abd ipv4
print("Socket Created")
# it will have two parameter one is ip address and second in port number
# bind use to bind a socket with a port number
# don't use port number that already use by some other services
server_socket.bind(('localhost', 9999))
# Maximum number of connection at one time with this server start listening to client
server_socket.listen(3)
print('Waiting for connections..')

while True:
    client_socket, address = server_socket.accept()
    name = client_socket.recv(1024).decode()
    print("Connected with", address, name)

    # it needs to be in byte format
    client_socket.send(bytes('Welcome to Connection', 'utf-8'))
    # one option for message and second is for what type of format you want to send
    client_socket.close()

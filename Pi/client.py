import sys
import socket

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except socket.error as err:
    print("Socket creation failed with error {}".format(err))

port = 12345
host_ip = ''

client.connect((host_ip, port))

print("socket connected to {}".format(host_ip))

client.send("Client connected".encode())

while True:
    from_server = client.recv(1024)
    print(from_server.decode())

client.close()

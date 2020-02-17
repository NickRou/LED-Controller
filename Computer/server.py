import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
except socket.error as err:
    print("Socket creation failed with error {}".format(err))

"""reserve port on Pi to 12345 and size to 1024"""
port = 12345
size = 1024

"""bind socket to port and listen to requests coming from computer on network"""
s.bind(('', port))
print("Socket bound to port {}".format(port))
s.listen(5)


while True:
    conn, addr = s.accept()
    data = conn.recv(size).decode()
    print(data)
    conn.send("Orange".encode())

conn.close()
sys.exit()


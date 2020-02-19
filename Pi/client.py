import socket
import sys
import time
import threading
from Pi.led_controls import LED
from neopixel import *

SOCKET_AMOUNT = 100
HOST = ''
PORT = 12345
SIZE = 1024

"""Testing new client and server configurations using multi processing and threading"""

def myclient(ip, port, message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
    except socket.error as err:
        print("Socket creation failed with error {}".format(err))

    s.connect((ip, port))
    s.sendall(message.encode())
    from_server = s.recv(SIZE)
    print("{0} final client time {1}".format(from_server.decode(), time.time()))
    s.close()

if __name__ == "__main__":
    threads = []
    for i in range(SOCKET_AMOUNT):
        msg = "Thread# {}, client time {}".format(i, time.time())
        client_thread = threading.Thread(target=myclient, args=(HOST, PORT, msg))
        threads.append(client_thread)
        client_thread.start()

    waiting = time.time()
    [x.join() for x in threads]
    done = time.time()
    print("Done {}. Waiting for {} seconds".format(done, done-waiting))



"""
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

"""
run this command in python terminal when in the rpi_ws281x/python directory
sudo PYTHONPATH=".:build/lib.linux-armv7l-2.7" python examples/strandtest.py
"""


strip = LED()

while True:
    from_server = client.recv(1024)
    print(from_server.decode())
    if from_server == 'Green':
        strip.colorWipe(Color(255, 0, 0))



client.close()

"""

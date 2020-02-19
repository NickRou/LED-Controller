import socket
import time
import multiprocessing

HOST = ''
PORT = 12345
SIZE = 1024


def handle(connection, address):
    try:
        while True:
            data = connection.recv(SIZE).decode()
            connection.sendall(data + ' server time {}'.format(time.time()).encode())
    except:
        pass
    finally:
        connection.close()


class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created")
        except socket.error as err:
            print("Socket creation failed with error {}".format(err))

        print("hello")

        s.bind((self.host, self.port))
        s.listen(1)

        print("hello")
        while True:
            conn, addr = s.accept()
            process = multiprocessing.Process(target=handle, args=(conn, addr))
            process.daemon = True
            process.start()


if __name__ == "__main__":
    server = Server(HOST, PORT)
    try:
        print("Starting server")
        server.start()
    except:
        print("Something went wrong or keyboard interrupt")
    finally:
        for process in multiprocessing.active_children():
            process.terminate()
            process.join()
        print("Serving shutting down")

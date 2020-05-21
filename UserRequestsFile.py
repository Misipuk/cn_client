import json
import socket

class UserRequest:

    def getCafes(self): #with Reviews
        pass

    def createCafe(self):
        pass

    def addReview(self): #with Reviews
        pass

    def delReview(self):#byReviewID
        pass

    def createCafe(self):
        pass

    def register(self, login: str, password: str):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', 9091))
        body = json.dumps({"login": login, "password": password})
        client_sock.sendall(b'POST /users HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Content-Length: ' + str(len(body)).encode() + b'\n')
        client_sock.sendall(b'\n')
        client_sock.sendall(body.encode())
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def login(self, login: str, password: str):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', 9090))
        body = json.dumps({"login": login, "password": password})
        client_sock.sendall(b'POST /login HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Content-Length: ' + str(len(body)).encode() + b'\n')
        client_sock.sendall(b'\n')
        client_sock.sendall(body.encode())
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def do_smth(self):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', 9090))
        client_sock.sendall(b'GET /users HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(
            b'Authorization: eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1ODk4Nzk0NjMsICJrZXkiOiAieHFrMmVJamJ3eFJzdDVtd3JaLVRHZnJvZTctUzF4ZXEzTzNxSW9CN0JWQT0ifQ==\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))
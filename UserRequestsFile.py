import json
import socket
from typing import Dict

PORT = 9091


class UserRequest:

    def getCafes(self):  # with Reviews
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'GET /cafes HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(
            b'Authorization: eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1ODk4Nzk0NjMsICJrZXkiOiAieHFrMmVJamJ3eFJzdDVtd3JaLVRHZnJvZTctUzF4ZXEzTzNxSW9CN0JWQT0ifQ==\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def getCafesMedia(self):  # with Reviews
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'GET /cafemedia HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(
            b'Authorization: eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1ODk4Nzk0NjMsICJrZXkiOiAieHFrMmVJamJ3eFJzdDVtd3JaLVRHZnJvZTctUzF4ZXEzTzNxSW9CN0JWQT0ifQ==\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def add_cafe_media(self, auth_token: str, cafe_id: int, file_to_img: str):  # with Reviews
        with open(file_to_img, mode='rb') as f:
            body = f.read()

        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'POST /cafe/media?cafe_id=%d&type=photo HTTP/1.1 \n' % cafe_id)
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(b'Authorization: %s\n' % auth_token.encode())
        client_sock.sendall(b'Content-Length: %d\n' % len(body))
        client_sock.sendall(b'\n')
        client_sock.sendall(body)
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def delCafeMedia(self):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'POST /delcafemedia HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(
            b'Authorization: eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1ODk4Nzk0NjMsICJrZXkiOiAieHFrMmVJamJ3eFJzdDVtd3JaLVRHZnJvZTctUzF4ZXEzTzNxSW9CN0JWQT0ifQ==\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def editCafe(self):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'POST /editcafe HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(
            b'Authorization: eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1ODk4Nzk0NjMsICJrZXkiOiAieHFrMmVJamJ3eFJzdDVtd3JaLVRHZnJvZTctUzF4ZXEzTzNxSW9CN0JWQT0ifQ==\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def createCafe(self):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'POST /createcafe HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(
            b'Authorization: eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1ODk4Nzk0NjMsICJrZXkiOiAieHFrMmVJamJ3eFJzdDVtd3JaLVRHZnJvZTctUzF4ZXEzTzNxSW9CN0JWQT0ifQ==\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def add_cafe_review(self, auth_token: str, review: Dict[str, str]):  # with Reviews
        body = json.dumps(review).encode()

        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'POST /cafe/review HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(b'Content-Length: %d\n' % len(body))
        client_sock.sendall(b'Authorization: %s\n' % auth_token.encode())
        client_sock.sendall(b'\n')
        client_sock.sendall(body + b'\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def delReview(self):  # byReviewID
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'POST /delreview HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(
            b'Authorization: eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1ODk4Nzk0NjMsICJrZXkiOiAieHFrMmVJamJ3eFJzdDVtd3JaLVRHZnJvZTctUzF4ZXEzTzNxSW9CN0JWQT0ifQ==\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def register(self, login: str, password: str):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
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

    def login(self, login: str, password: str) -> str:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
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
        # TODO
        return "eyJsb2dpbiI6ICJsIiwgImV4cGlyZSI6IDE1OTAwODM5OTMsICJrZXkiOiAiRWpNcUVlUmpzMVpuMldvcDlSRkVyeE5ZcXBTclpGMURXcVpXaE9vNTE5QT0ifQ=="

    def get_users(self, auth_token: str):
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'GET /users HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(b'Authorization: %s\n' % auth_token.encode())
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

    def add_cafe(self, auth_token: str, cafe: Dict[str, str]):
        body = json.dumps(cafe).encode()

        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('localhost', PORT))
        client_sock.sendall(b'POST /cafe?kek=kek HTTP/1.1 \n')
        client_sock.sendall(b'Host: MyServer\n')
        client_sock.sendall(b'Accept: application/json\n')
        client_sock.sendall(b'Content-Length: %d\n' % len(body))
        client_sock.sendall(b'Authorization: %s\n' % auth_token.encode())
        client_sock.sendall(b'\n')
        client_sock.sendall(body + b'\n')
        client_sock.sendall(b'\n')
        data = client_sock.recv(1024)
        client_sock.close()
        print('Received', repr(data))

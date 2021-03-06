#!/usr/bin/env python
# encoding=utf-8

import socket

SERVER_ADDRESS = (HOST, PORT) = "", 8888


def run_server():
    """
    启动服务
    """
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen()
    print("Server HTTP on port %s" % PORT)

    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print(request.decode('utf-8'))

        http_response = b"""\
HTTP/1.1 200 OK

Hello World From simple socket server!
"""
        client_connection.sendall(http_response)
        client_connection.close()


if __name__ == '__main__':
    run_server()

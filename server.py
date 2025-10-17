

import socket

HOST = "127.0.0.1"  # loopback (locahost) interface address
PORT = 65432  # port to listen on 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Listening on 127.0.0.1:65432\n")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            print("Request data received : ", data, "\n")
            

            print("Got a request!")




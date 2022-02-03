import socket
import os
from time import sleep

path = "rem/"

def in_path():
    if filename in os.listdir(path):
        return True
    return False

def is_modified(name,mtime):
    mtime = float(mtime)
    if os.path.getmtime(path+name) < mtime:
        return True
    return False

def copy_file(conn):
    sleep(0.1)
    conn.send(b"c")
    f = open(filename,"wb")
    while True:
        data = conn.recv(1024)
        if data == b'':
            f.close()
            conn.close()
            break
        else:
            f.write(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.36",9000))
s.listen()

while True:
    conn, addr = s.accept()
    file = conn.recv(1024)
    print("file =",file)
    print("[SERVER] Query received.")
    file = file.decode("utf-8")
    file = file.split()

    filename = path+file[0]
    print("filename",filename)
    print("FILE",file)

    print("[SERVER] Checking the file.")
    if in_path():
        if is_modified(file[0],file[1]):
            print("[SERVER] Copying the file")
            copy_file(conn)
            print("[SERVER] Done!")
    else:
        print("[SERVER] Copying the file")
        copy_file(conn)
        print("[SERVER] Done!")
        


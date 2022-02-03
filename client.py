import socket
import os

path = "loc/"

def send_file(file):
    f = open(file,"rb")
    data = f.read(1024)
    while True:
        s.send(data)
        data = f.read(1024)
        if data == b'':
            break

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.36",9000))

listf = os.listdir(path)
print("listf =",listf)
for i in listf:
    print("i =",i)
    mtime = os.path.getmtime(path+i) 
    msg = i+" "+str(mtime)
    print(msg)
    msg = msg.encode("utf-8")
    s.send(msg)
    print("[CLIENT] Consulting the server.")
    ins = s.recv(1024)
    if ins == b'c':
        print("[CLIENT] Sending the file...")
        send_file(path+i)
        print("[CLIENT] Done!")
print("FIN")

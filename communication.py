import socket
import time

HOST = 'localhost'
PORT = 42001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def sendCMD(cmd):
    s.send(len(cmd).to_bytes(4, 'big'))
    s.send(bytes(cmd, 'UTF-8'))

sendCMD('broadcast "hello"')

time.sleep(1)

for i in range(10):
    time.sleep(0.1)
    data = s.recv(64)
    if not data:
        break
    print(data[4:].decode('UTF-8'))
    
s.close()

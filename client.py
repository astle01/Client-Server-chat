
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',1234))

msg = s.recv(2048).decode()

print(msg)

msg = input("enter something :")
s.send(msg.encode())

while msg!='quit':
    msg = s.recv(2048).decode()
    print(msg)
   
    msg = input("enter something :")
    s.send(msg.encode())

s.close()

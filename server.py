
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',1234))

s.listen(3)

c,address = s.accept()
print("connection recieved from {} ".format(address))

banner = "Hi this is server!"
c.send(banner.encode())

msg = c.recv(2048).decode()

while msg!='quit':
    print(msg)
    msg = input("enter something:")
    c.send(msg.encode())
    
    msg = c.recv(2048).decode()

c.close()

s.close()

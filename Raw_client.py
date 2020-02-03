import socket
print("Client version 0.1")
addr = ("", 8080)
s = socket.create_connection(addr)
while True:
    s.send((input()).encode())
    

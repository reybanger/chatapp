import socket
import threading 
from Server import threading

def ConnectToServer(addr):
    s = socket.create_connection(addr)
    return s
def Messaging_send(Peer):
    while True:
        Peer.send((input().encode()))
def Messaging_recv(Peer):
    while True:
        print(Peer.recv(1024).decode())

def Main():
    addr = ("", 8080)
    Connection = ConnectToServer(addr)

    ReceiveThread = threading.Thread(target=Messaging_recv, args=(Connection,))
    ReceiveThread.start()
    SendThread = threading.Thread(target=Messaging_send, args=(Connection,))
    SendThread.start()
    
    
   

#Main function init 
if __name__ == '__main__':
    print("Client version 0.2")
    Main()
    








 







    

    






import socket
import threading 
from Server import threading

def GetUser():
    UserNr = input("Podaj swoj numer:\n")
    return UserNr
def ConnectToServer(addr):
    s = socket.create_connection(addr)
    return s
def Messaging_send(Peer):
    while True:
        Peer.send((input().encode()))
def Messaging_recv(Peer):
    while True:
        print(sClientSocket.recv(1024))

def Main():
    addr = ("", 8080)
    Nr = GetUser()
    Connection = ConnectToServer(addr)
    thread = threading.Thread(target=Messaging_send, args=(Connection,))
    #thread2 = threading.Thread(target=Messaging_recv, args=(Connection,))
   

#Main function init 
if __name__ == '__main__':
    print("Server version 0.2")
    Main()
    








 







    

    






import socket
import threading 
from Server import threading

#Tworzy server socket, ktory bedzie akcepptowal polaczenia
def StartServer(addr):
    ServerSocket = socket.create_server(addr)
    return ServerSocket

#Akceptuje polaczenie z serwerem i zwraca nowy socket 
def AcceptConnection(ServerSocket):
    ClientConn = ServerSocket.accept()[0]
    return ClientConn
#Wiadmosci - watek


def ReceiveDataFrom(sClientSocket):
    while True:
        print(sClientSocket.recv(1024))

#Glowna funkcja
def Main():
    addr = ("", 8080)
    Server = StartServer(addr)
    Client = AcceptConnection(Server)
    ReceiveDataFrom(Client)

if __name__ == '__main__':
    print("Server version 0.1")
    Main()
    
    








 







    

    




#print ("Listuj� liczby z przedia�u"+str(a)+" "+str(b)+" ")

#test = int(input())
#print (test)
#if test < 18: print("Malolat!")
#else: print("Dorosly!")
#for character in str(test):
#    print (character)




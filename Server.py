import socket
import threading 
from Server import threading

#Lista podlaczonych uzyszkodnikow - niby globalna, a nie dziala 
Users = []

def PrintUsers(sClientSocket):
    sClientSocket.send(("====== User list ======\n").encode())
    for user in Users:
        sClientSocket.send((user+"\n").encode())

#Tworzy server socket, ktory bedzie akcepptowal polaczenia
def StartServer(addr):
    ServerSocket = socket.create_server(addr)
    return ServerSocket

def ReceiveDataFrom(sClientSocket):
    while True:
        data = sClientSocket.recv(1024).decode()
        print(data)
        if data == "!users":
            PrintUsers(sClientSocket)

#Lista aktualnie podłączonych numerów
def AddConnectedUsers(User):
    Users.append(User) 

#Akceptuje polaczenie z serwerem i zwraca nowy socket 
def AcceptConnection(sServerSocket):
    ClientConn, ClientAddr = sServerSocket.accept()
    print ("Connected: ", ClientAddr)
    ClientConn.send(("Welcome to server. Insert commands after '!'".encode()))
    ClientConn.send(("Provide your ID".encode()))
    ClientID = ClientConn.recv(1024).decode()
    print ("Client ID: ", ClientID, " connected.")
    AddConnectedUsers(ClientID)
    ReceiveDataFrom(ClientConn)
    return 0


#Glowna funkcja
def Main():
    addr = ("", 8080)
    Server = StartServer(addr)
    #Watek kliencki
    Threads = []
    for i in range(5):
        thread = threading.Thread(target=AcceptConnection, args=(Server,))
        Threads.append(thread)
        thread.start()

        
       
#Main function init 
if __name__ == '__main__':
    print("Server version 0.1")
    Main()
    
    








 







    

    





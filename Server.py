import socket
import threading 
from Server import threading

#Global list of users. Tuple (Socket,ID)
Users = []

#Sends currently connected users to the server
#Needs adjustment TODO
def PrintUsers(sClientSocket):
    sClientSocket.send(("====== Connected users: ======\n").encode())
    for user in Users:
        sClientSocket.send((user[1]+"\n").encode())

#Tworzy server socket, ktory bedzie akceptowal polaczenia
def StartServer(addr):
    ServerSocket = socket.create_server(addr)
    return ServerSocket

#Message broadcasting
def BroadcastMessage(strMessage,tClient):
    for client in Users:
        if client != tClient:
            client[0].send((str(tClient[1])+" godo: "+strMessage).encode())

#To prawdopodobnie potrzebuje drugiego socketa jako argument, aby serwer mógł poprawnie robić relay wiadomości
#Takes tuple - socket, ID
def ReceiveDataFrom(tClientSocket):
    while True:
        data = tClientSocket[0].recv(1024).decode()
        print(data)
        BroadcastMessage(data,tClientSocket)
        if data == "!users":
            PrintUsers(tClientSocket[0])

#Lista aktualnie podłączonych numerów. Tuple socket-ID
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
    tClient = (ClientConn, ClientID)
    AddConnectedUsers(tClient)
    ReceiveDataFrom(tClient)
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
    
    








 







    

    





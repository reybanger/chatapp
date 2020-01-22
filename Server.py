import socket
import threading 
from Server import threading

#Tworzy server socket, ktory bedzie akcepptowal polaczenia
def StartServer(addr):
    ServerSocket = socket.create_server(addr)
    return ServerSocket


def ReceiveDataFrom(sClientSocket):
    while True:
        print(sClientSocket.recv(1024))

#Akceptuje polaczenie z serwerem i zwraca nowy socket 
def AcceptConnection(sServerSocket):
    ClientConn, ClientAddr = sServerSocket.accept()
    print ("Connected: ", ClientAddr)
    ReceiveDataFrom(ClientConn)
    return 0





#Glowna funkcja
def Main():
    addr = ("", 8080)
    #Server = threading.Thread(target=StartServer,args=addr)
    #Server.start()
    Server = StartServer(addr)
    #Watek kliencki
        T1 = threading.Thread(target=AcceptConnection, args=(Server,))
        T1.start()
    


#Main function init 
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




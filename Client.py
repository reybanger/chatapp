import socket
print("Client version 0.1")
addr = ("", 8080)
s = socket.create_connection(addr)
while True:
    s.send((input()).encode())
    








 







    

    




#print ("Listuj� liczby z przedia�u"+str(a)+" "+str(b)+" ")

#test = int(input())
#print (test)
#if test < 18: print("Malolat!")
#else: print("Dorosly!")
#for character in str(test):
#    print (character)




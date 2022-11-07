import socket
print(socket.gethostbyname('sherpurgovtcollege.edu.bd'))

TARGET = input("enter a word : ") or ("hello word")
port = input("Enter port or just click enter for default : ") or  80
 
print(type (port))
import socket
import json

#creating socket
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', PORT))    #connecting the port with the localhost machine
s.listen(1) # server listens to one client

conn, addr = s.accept()  # accepting the connection
data = conn.recv(1024)  # receives data

#converting the type of 'data' from byte to string, and then to dictionary
ss = data.decode()
user = json.loads(ss)

print("Name: " + user['name'])      #printing user's data  while accessing specific key in json format
print("Age: " + user['age'])
print("Matrikelnummer: " + user['Matnummer'])

conn.close()        #closing the connection of the socket


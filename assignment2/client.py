import socket

#creating the socket
PORT = 8080
s = socket.socket()
s.connect(('localhost', PORT))

#User enters data
print("Enter your name: ")
name = input(" -> ")
print("Enter your age: ")
age = input(" -> ")
print("Enter your Matrikelnummer: ")
matnum = input (" -> ")

#creating json format string and sending the data
dataaa = '{"name":"' +name + '",'' "age":"' +age + '",'' "Matnummer":"' +matnum + '"''}'
s.sendall((dataaa).encode('utf-8'))
s.close()       #closing the socket connection with the server
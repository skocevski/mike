import socket

#creating the socket
PORT = 8080
s = socket.socket()
s.connect(('localhost', PORT))

#User enters URL until URL ends with  \r\n
url=""
while True:
    print("Pleas Enter a URL:")
    url = input('->')
    if (url[len(url) - 4:len(url)]=='\\r\\n'):
        break

print("The following URL was sent to server: ")
print(url)
s.send(url.encode('utf-8')) #sending url variable over socket





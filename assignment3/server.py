import socket

#creating socket
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', PORT))    #connecting the port with the localhost machine
s.listen(1) # server listens to one client

conn, addr = s.accept()  # accepting the connection
tmp = conn.recv(1024)

url = tmp.decode('utf-8')

i=0
protocol = ""
subdomain=""
domain=""
port=""
full_path=""
param=""
fragment=""


if (len(url)>0):
# splitting the protocol part of the url
    while(url[i:i+3]!= "://"):
        protocol = protocol + url[i]
        i = i + 1
    print("Protocol: \t" + protocol)
    i = i + 3

#splitting the domain part
    array=[]
    while (url[i] != "/" and  url[i] != ":"):
        domain=domain + url[i]
        i=i+1
    print("Domain: \t" +domain)

#splitting the subdoman part
    sub = domain.split(".")
    j=0
    while (j<len(sub) -2 ):
        subdomain = subdomain + sub[j] + ", "
        j=j+1
    print("Sub-domain:\t" + subdomain)

#splitting the port (if there is any in the url)
    if(url[i]==":"):
        while(url[i]!= "/"):
            port=port+url[i]
            i=i+1
    else:
        port="No port was specified!"
        i=i+1
    print("Port: \t\t" + port)

#splitting the full_path part
    while (url[i] != "?" and url[i:i+4] != "\\r\\n"):
        full_path = full_path + url[i]
        i = i + 1
    print("Full path: \t" + full_path)

#splitting the parameters
    i=i+1
    while (url[i] != "#" and url[i-1:i+3] != "\\r\\n"):
        if(url[i]=="&"):
            param = param + '\n \t\t\t'
        else:
            param = param + url[i]
        i = i + 1
    print("Parameters:\t" + param)

#splitting the fragments
    while (url[i-1:i+3] != "\\r\\n"):
        fragment = fragment + url[i]
        i = i + 1
    print("Fragments: \t" + fragment[1:len(fragment)-1])

else:
    print("No URL was received!")

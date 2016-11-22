import socket
from urllib.parse import urlparse
import sys
import time

#function timeout for getting the entire data from the file
def recv_timeout(the_socket, timeout=2):
    # make socket non blocking
    the_socket.setblocking(0)
    # total data partwise in an string
    totalData=""
    data = '';
    # beginning time
    begin = time.time()
    while 1:
        # if we got some data, then break after timeout
        if totalData and time.time() - begin > timeout:
            break

        # if you got no data at all, wait a little longer, twice the timeout
        elif time.time() - begin > timeout * 2:
            break

        # recv something
        try:

            data = the_socket.recv(8192)
            if data:
                totalData = totalData + data.decode()
                # change the beginning time for measurement
                begin = time.time()
            else:
                # sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
    if(totalData.find("200 OK") != -1):
        seperate(totalData)
    else:
        print("The status of the HTTP response was other then 200 OK. \n Could not be processed!")
    # return 0 for successfully executed function
    return 0


def seperate(list_to_Separate):

    splitted = str(list_to_Separate).split('\r\n\r\n')
    print(splitted[0])
    #writing data from the HTTP header
    iphph = open("index.php.header", "w")
    iphph.write(splitted[0])
    iphph.close()
    #writing data from the HTTP body
    iphp = open("index.php", "w")
    iphp.write(splitted[1])
    iphp.close()
    return 0


url=input("Enter URL:")
o = urlparse(url)

host=o.netloc
path=o.path

port = 80  # web

print('\n # Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print('# Getting remote IP address')
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip, port))

# Send data to remote server
print('# Sending data to server')
request = "GET "+ path +" HTTP/1.0\r\n\r\n"

try:
    s.sendall(request.encode('utf'))
except socket.error:
    print
    'Send failed'
    sys.exit()

# Receive data
print('# Receive data from server \n ')
recv_timeout(s)

s.close()
print ("\ndone")


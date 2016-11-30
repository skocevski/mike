import wget
import re
from urllib.parse import urlparse
import urllib.request
import socket
import time
import queue

def doHTTPRequest(url):

    o = urlparse(url)
    host = o.netloc
    path = o.path
    file_name = url.split('/')[-1]
    print(file_name)
    port = 80  # web
    urlQueue.put(url)

    while not urlQueue.empty():
        print('\n # Creating socket')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print('# Getting remote IP address')
        remote_ip = socket.gethostbyname(host)

        print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
        s.connect((remote_ip, port))

        print('# Sending data to server')
        request = "GET " + path + " HTTP/1.0\r\n\r\n"
        s.sendall(request.encode('utf'))

        print('# Receive data from server \n ')
        HTMLcontent = recv_timeout(s)
        links = findURLS(HTMLcontent)
        downloadFILE(links, HTMLcontent)

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
        splitted = str(totalData).split('\r\n\r\n')
        htmlbody = splitted[1]
    # return 0 for successfully executed function
    return htmlbody


def downloadFILE (links, HTMLcontent):
    i = 0
    while (i < len(links)):
        o = urlparse(links[i])
        hst = o.netloc
        if (hst == "141.26.208.82"):
            fnn = links[i].split('/')[-1]
            file_ = open(fnn, 'w')
            file_.write(str(HTMLcontent.encode('utf-8')))
            file_.close()
            urlQueue.put(links[i])
        i = i + 1

def findURLS(content):
    RegExpr = '<a href="?\'?([^"\'>]*)'
    links = re.findall(RegExpr, content)
    print(len(links))
    i = 0  # printing and download the images
    j=0
    while (i < len(links)):
        links[i] = urllib.parse.urljoin("http://141.26.208.82", str(links[i]))
        i = i + 1

    return links


f = 'http://141.26.208.82/articles/g/e/r/Germany.html'
urlQueue = queue.Queue()
doHTTPRequest(f)

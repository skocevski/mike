import socket  # Networking support
import signal  # Signal support (server shutdown on signal receive)
import time    # Current time
import os

class Server:

 def __init__(self, port = 80):
     self.host = 'localhost'
     self.port = port
     self.www_dir = os.getcwd()
    
  
 def activate_server(self):
     self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     try:
         self.socket.bind((self.host, self.port))
     except Exception as e:
         user_port = self.port 
         self.port = 8080
         
         try:
             self.socket.bind((self.host, self.port))
             
         except Exception as e:
             self.shutdown()
             import sys
             sys.exit(1)

     print ("Server successfully acquired the socket with port:", self.port)
     self._wait_for_connections()
  
 def shutdown(self):
     try:
         s.socket.shutdown(socket.SHUT_RDWR)
     except Exception as e:
         print("Warning: could not shut down the socket. Maybe it was already closed?",e)


 def _gen_headers(self,  code):

     header = ''
     if (code == 200):
         header = 'HTTP/1.1 200 OK\n'
     elif(code == 404):
         header = 'HTTP/1.1 404 Not Found\n'
     current_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
     header += 'Date: ' + current_date +'\n' + 'Server: Simple-Python-HTTP-Server\n' + 'Connection: close\n\n'  # signal that the conection wil be closed after complting the request

     return h

 def _wait_for_connections(self):

     while True:
         print ("Awaiting New connection")
         self.socket.listen(3) # maximum number of queued connections
         conn, addr = self.socket.accept()
         data = conn.recv(1024) #receive data from client
         string = bytes.decode(data) #decode it to string

         request_method = string.split(' ')[0]
         print ("Method: ", request_method)
         print ("Request body: ", string)

         if (request_method == 'GET') | (request_method == 'HEAD'):
             file_requested = string.split(' ')
             file_requested = file_requested[1] # get 2nd element
             file_requested = file_requested.split('?')[0]  # disregard anything after '?'

             if (file_requested == '/'):  # in case no file is specified by the browser
                 file_requested = '/index.html' # load index.html by default
             
             elif(file_requested != '/wait_for_server'):
                 
                 file_requested = self.www_dir + file_requested
                 print ("Serving web page [",file_requested,"]")
                 try:
                     file_handler = open(file_requested,'rb')
                     if (request_method == 'GET'):  #only read the file when GET
                         response_content = file_handler.read() # read file content                       
                     file_handler.close()
                 
                     response_headers = self._gen_headers( 200)          
                 
                 except Exception as e: #in case file was not found, generate 404 page
                     print ("Warning, file not found. Serving response code 404\n", e)
                     response_headers = self._gen_headers( 404)
             
                     if (request_method == 'GET'):
                         response_content = b"<html><body><p>Error 404: File not found</p><p>Python HTTP server</p></body></html>"  

                 server_response =  response_headers.encode() # return headers for GET and HEAD
                 if (request_method == 'GET'):
                     server_response +=  response_content  # return additional conten for GET only


                 conn.send(server_response)
                 print ("Closing connection with client")
                 conn.close()
             else:
                 inpt = input("server input: ")
                 conn.send(inpt.encode())
         else:
             print("Unknown HTTP request method:", request_method)


print ("Starting web server")
s = Server(80)  # construct server object
s.activate_server() # aquire the socket
    


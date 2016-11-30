import socket
import os
def url_processor(Input):
    protocol, port, path, Frag, param= []
    index, Flag = 0
    if "://" in Input:
        Flag = 1
    while index < len(Input) and Flag == 1 and Input[index] != ':':
        protocol.append(Input[index])
        index += 1
    if Flag == 1:
        index += 1
    while Input[index] == '/' or Input[index] == ' ':
        index += 1
    j = index
    while index < len(Input) and Input[index] not in [':', '/']:
        index += 1
    portflag = 0
    if index < len(Input) and Input[index] == '/':
        portflag = 1
    index += 1
    names = Input[j:index - 1]
    names = names.split(".")
    while index < len(Input) and Input[index] != '/' and portflag == 0:
        port.append(Input[index])
        index += 1
    if portflag == 0:
        index += 1
    while index < len(Input) and Input[index] != '?':
        path.append(Input[index])
        index += 1
    index += 1
    while index < len(Input) and Input[index] != '#':
        param.append(Input[index])
        index += 1
    index += 1
    while index < len(Input):
        Frag.append(Input[index])
        index += 1
    return protocol, names, port, path, param, Frag

def Header_seperator(file_name, string):
    try:
        content = open(file_name, "wb")
        splited_str = string.split(b"\r\n\r\n", 1)
        header = splited_str[0]
        header = header.split(b' ')
        if header[1] != b'200':
            return -1
        splited_str[1] = splited_str[1].replace(b'\\n', b'')
        splited_str[1] = splited_str[1].replace(b'\\t', b'')
        content.write(splited_str[1])
        content.close()
        return 0
    except Exception as ex:
        print("header_seperator : ", ex)
def response(socket, file_name):
    answer = bytearray()
    try:
        tmp = socket.recv(8196)
        while tmp != b'':
            for char in tmp:
                answer.append(char)
            tmp = socket.recv(8196)
        socket.close()
        flag = Header_seperator(file_name, answer)
        return flag
        print("Task Finished")
    except Exception as ex:
        print("response ", ex)
def file_to_string(file_name):
    file = open(file_name, "r")
    string = ""
    for item in file:
        string += item
    file.close()
    return string
def string_parser(string, start, end):
    index = string.find(start)
    answer = []
    while True:
        if index == -1:
            break
        end_index = string[index + len(start):].find(end)
        i = index + len(start) + end_index + len(end)
        answer.append(string[index:i])
        string = string[index + len(start) + end_index + len(end):]
        index = string.find(start)
    return answer
def client(socket, url, file_name):
    protocol, names, port, path, param, Frag = url_processor(url)
    protocol = "".join(protocol)
    if len(protocol) != 0 and protocol.upper() != "HTTP":
        print("This is HTTP Client program!")
        return
    server = ""
    for name in names:
        server += name + "."
    path = "".join(path)
    server = server[0:len(server) - 1]
    try:
        socket.connect((server, 80))
    except:
        print("not connected ")
    if len(path) == 0:
        get = b"GET /HTTP/1.1\r\n\r\n "
        print(get)
    else:
        get = b"GET /" + path.encode() + b" /HTTP/1.1\r\n\r\n"
    try:
        socket.sendall(get)
    except:
        print("data can not be sent!")
    flag = response(socket, file_name)
    return flag
def extract(file_name):
    try:
        links = []
        tmp = ""
        str_temp = file_to_string(file_name)
        i = 1
        index = 0
        split_data = str_temp.split("<a")
        while i < len(split_data):
            string = split_data[i]
            index = string.find('href="')
            if index != -1:
                index += len('href="')
                while string[index] != '"':
                    tmp += string[index]
                    index += 1
                links.append(tmp)
                tmp = ""
            i += 1
        return links
    except:
        return []
def merg_3(src, dest, array):
    for item in src:
        if item not in array.keys():
            dest.append(item)
            array[item] = 1
def correct_url(string):
    i = 0
    while i < len(string):
        if string[i] in ['.', '/']:
            i += 1
        else:
            break
    return string[i - 1:]
def get_request(url, file_name):
    import socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    flag = client(socket, url, file_name)
    return flag
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = "http://141.26.208.82/articles/g/e/r/Germany.html"
get_request(url, "pages/level_0_1.html")
all_links = {}
Total_number_of_pages = 0
level = 0
Internal_pages_count = {}
external_pages_count = {}
while True:
    n = 1
    file_name = "pages/level_" + str(level) + "_" + str(n) + ".html"
    current_links = []
    while os.path.isfile(file_name):
        temp = extract(file_name)
        merg_3(temp, current_links, all_links)
        n += 1
        Total_number_of_pages += 1
        file_name = "pages/level_" + str(level) + "_" + str(n) + ".html"
    index = 1
    print(len(current_links))
    if len(current_links) == 0:
        break
    for link in current_links:
        if link[0] in ['.', '/']:
            url = correct_url(link)
            url = "http://141.26.208.82" + url
            file_name = "pages/level_" + str(level + 1) + "_" + str(index) + ".html"
            flag = 0
            flag = get_request(url, file_name)
            if flag == 0:
                index += 1
    level = level+ 1

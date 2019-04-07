import os

file_path = "c:\\Users\\rabia\\Documents\\programs\\python\\cryptopals\\cryptopal-challenges\\Set_1\\textFiles\\"
filesList = ['ch4.txt', 'ch6.txt', 'ch7.txt', 'ch8.txt']

fileMap = {file:file_path+file for file in filesList}

def load_file(fileName):

    f = open(fileMap[fileName], "r")
    
    return list(line.rstrip() for line in f)

def KeyExpansion(key, msg_len):

    if type(key) != bytes:
        raise TypeError("Key needs to be a bytes string not %s" % type(key))
    if type(msg_len) != int:
        raise TypeError("Message Length defined as integer not %s" % type(msg_len))
    
    q, r = divmod(msg_len,len(key))

    return q * key + key[:r]
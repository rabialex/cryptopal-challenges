import os

file_path = "c:\\Users\\rabia\\Documents\\programs\\python\\cryptopals\\challenges\\cryptopal_challenges\\Set_1\\textFiles\\"
filesList = ['ch4.txt', 'ch6.txt', 'ch7.txt', 'ch8.txt']

fileMap = {file:file_path+file for file in filesList}

def load_file(fileName):

    f = open(fileMap[fileName], "r")
    
    return list(line.strip("\n") for line in f)
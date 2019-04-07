"""
Challenge4: Detect single-character XOR
    Given a file of hex encoded string that has been xor'd 
    agains a single character. The goal is to  
    find and decrypt the message. 
"""
from challenge3 import breakSingleXOR
from helper import load_file

# decode the lines in the file 
fileList = load_file("ch4.txt")
fileList = list(bytes.fromhex(hexString) for hexString in fileList)

# first for each line return the broken XOR

brokenList = []

for i in range(len(fileList)):

    temp = breakSingleXOR(fileList[i])
    if i == 170:
        print(temp)


key = lambda x: x[-1]
sorted(brokenList, key =key, reverse =True)

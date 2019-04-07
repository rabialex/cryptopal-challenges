"""
Challenge4: Detect single-character XOR
    Given a file of hex encoded string that has been xor'd 
    agains a single character. The goal is to  
    find and decrypt the message. 
"""
from challenge3 import breakSingleXOR
from helper import load_file

# decode the lines in the file 
fileList = list(bytes.fromhex(line) for line in load_file("ch4.txt"))


# first for each line return the broken XOR

brokenList = []

for cipherText in fileList:

    plaintext = breakSingleXOR(cipherText)
    brokenList.append(plaintext)

key = lambda x: x[-1]
sorted(brokenList, key =key, reverse =True)
breakpoint()
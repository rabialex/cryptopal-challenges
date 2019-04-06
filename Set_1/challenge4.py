"""
Challenge4: Detect single-character XOR
    Given a file of hex encoded string that has been xor'd 
    agains a single character. The goal is to  
    find and decrypt the message. 
"""
from helper import load_file

fileList = load_file("ch4.txt")
print(len(fileList))
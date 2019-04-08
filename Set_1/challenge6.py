from helper import load_file, KeyExpansion
from challenge2 import xor
from challenge3 import commonLetterScore

import pprint
import base64

def partition(string, keySize):

    partDict = dict((i, []) for i in range(keySize))

    for idx in range(len(string)):

        i = idx % keySize
        partDict[i].append(string[idx])
    
    return partDict

def ioc(string):

    try:
        string = string.replace(" ","").replace("\n","").lower() 
    except:
        pass

    freqDict = {}
    
    for c in string:
        if c in freqDict.keys():
            freqDict[c] += 1
        else:
            freqDict[c] = 1
    
    p = 0
    n = len(string)

    for v in freqDict.values():
        p += (v/n)**2
    
    return p

def findKeySize(cipherText, keySizeMax):

    keyScore = []

    for i in range(2, keySizeMax):

        partCipher = partition(cipherText, i)
        IOC = ioc(partCipher[0])
        keyScore.append((i, IOC))

    
    keyScore = sorted(keyScore, key = lambda x: x[-1], reverse=True)
    
    return keyScore

def breakVigenere(cipherText, keySize, idx = 0):

    cipherPart = partition(cipherText, keySize)
    possibleKey = []

    for part in cipherPart.values():

        part = bytearray(part)

        possibleKey.append(breakSingleXOR(part)[1])
    
    
    return "".join(possibleKey)


if __name__ == "__main__":
    
    cipherText = "".join(load_file("ch6.txt"))
    cipherText = base64.b64decode(cipherText)

    check = findKeySize(cipherText, 40)
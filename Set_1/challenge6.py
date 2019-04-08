def partition(string, keySize):

    if type(string) != str or type(keySize) != int:
        raise TypeError("Inputs are defined as string and integers not %s and %s" % type(string), type(keySize))

    partDict = dict((i, []) for i in range(keySize))

    for idx in range(len(string)):

        i = idx % keySize
        partDict[i].append(string[idx])
    
    return partDict

def ioc(string):

    if type(string) != str:
        raise TypeError("Input defined as string not %s" % type(string))

    string = string.replace(" ","").replace("\n","").lower()  
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

testString = """To be, or not to be, that is the question—
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them?
William Shakespeare - Hamlet"""

print(testString.replace(" ","").replace("\n",""))
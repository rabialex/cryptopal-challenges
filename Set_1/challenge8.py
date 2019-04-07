from helper import load_file

import pprint

def reps(cipherText, block):

    repDict = {}

    for idx in range(0, len(cipherText), block):
        
        substring = cipherText[idx: idx + block]

        if substring in repDict.keys():
            repDict[substring] += 1
        else:
            repDict[substring] = 0

    return sum(repDict.values())

def ecb_detector(cipherText, block):

    rep_check = reps(cipherText, block)
    if rep_check > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    
    block = 16
    cipherText = load_file("ch8.txt")

    for cp in cipherText:
        
        ecb = ecb_detector(cp, block)

        if ecb:
            ecb_encoded = cp
            break
    
    print("ECB ENCODED MESSAGE:\n",ecb_encoded,"\n")


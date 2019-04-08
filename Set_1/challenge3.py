"""
Challenge3: Single-byte XOR Cipher
    Given a hex encoded string that has been xor'd 
    agains a single character. The goal is to  
    decrypt the message. 
"""

from challenge2 import xor
from helper import KeyExpansion

def commonLetterScore(string):
    commonLetters = "ETAOINSHRDLU"
    vowels = 'aeiou'

    score = 0
    for c in string:
        if c.upper() in commonLetters:
            score += 1 
        if c in vowels:
            score += 2
    return score

def breakSingleXOR(ciphertext):

    msg = ""
    highScore = -1
    k = -1

    n = len(ciphertext)
 
    for key in range(256):

        KEY = KeyExpansion(chr(key).encode(), n)
        plaintext =  xor(ciphertext, KEY).decode(errors="ignore")

        try:
            if plaintext[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                score = commonLetterScore(plaintext)
                if score > highScore:
                    highScore = score
                    msg = plaintext
                    k = chr(key)
        except:
            pass
    return (msg, k, highScore)


if __name__ == "__main__":

    # encode the ciphertext as bytes
    cipherText = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    cipherText = bytes.fromhex(cipherText)
    broken_cipher = breakSingleXOR(cipherText)
    print(broken_cipher)
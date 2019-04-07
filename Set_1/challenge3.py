"""
Challenge3: Single-byte XOR Cipher
    Given a hex encoded string that has been xor'd 
    agains a single character. The goal is to  
    decrypt the message. 
"""

from challenge2 import xor

def commonLeterScore(string):
    commonLetters = "ETAOINSHRDLU"
    vowels = 'aeiou'

    score = 0
    for c in string:
        if c.upper() in commonLetters:
            score += 1 
        if c in vowels:
            score += 1
    return score

def keyExpansion(n, key):
    q, r = divmod(n, len(key))
    return q * key + key[:r]

def breakSingleXOR(ciphertext):

    msg = ""
    highScore = 0
    k = -1

    n = len(ciphertext)

    possible_plaintext = []

    for key in range(256):

        KEY = keyExpansion(n, chr(key).encode())
        plaintext =  xor(ciphertext, KEY).decode(errors="ignore")

        if plaintext == "":
            return(plaintext, k, highScore)

        if plaintext[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and " " in plaintext:
            score = commonLeterScore(plaintext)
            if score > highScore:
                highScore = score
                msg = plaintext
                k = chr(key)
            
    return (msg, k, highScore)


if __name__ == "__main__":

    # encode the ciphertext as bytes
    cipherText = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    cipherText = bytes.fromhex(cipherText)
    broken_cipher = breakSingleXOR(cipherText)
    print(broken_cipher)
"""
Challenge 5: Implement repeating-key XOR
    Using the key word implement a 
    repeating key XOR
"""
from helper import KeyExpansion
from challenge2 import xor

answer = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

def vigenereCipher(msg, key):

    if type(msg) != bytes:
        raise TypeError("message defined as bytes not %s" %type(msg))
    
    n = len(msg)
    KEY = KeyExpansion(key, n)

    return xor(msg, KEY)

if __name__ == "__main__":
    
    stanza = [
        "Burning 'em, if you ain't quick and nimble",
        "I go crazy when I hear a cymbal"
        ]
    stanza = "\n".join(stanza).encode()

    key = b"ICE"

    check = vigenereCipher(stanza, key).hex()

    print(check==answer)

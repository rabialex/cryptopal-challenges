'''
Set1 Basics Challenge1: base64 to hexadecimal encoding
Warning always perform operations on raw bytes and never on encoded
information 
'''
import base64

def bytes2base64(byteString):

    '''
    Input: A byte string 
    Returns: A byte string base64 encoded
    '''
    return base64.b64encode(byteString)


if __name__ == "__main__":

    hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    EncodedHex = bytes.fromhex(hex)
    print("Does the encoded string match: ", answer == bytes2base64(EncodedHex).decode())
    

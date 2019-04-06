"""
Challenge2: Fixed XOR
    Given two equal buffers produce their XOR.
    The buffers are hex encoded and must be 
    converted to bytes before xor
"""

def xor(buffer1, buffer2):

    '''
    Input: two decoded byte strings
    Output: A byte string of the XOR 
            product of the byte strings
    '''

    assert type(buffer1) == bytes and type(buffer2) == bytes, "TypeERROR input must be of type bytes"

    return bytes(i^j for i,j in zip(buffer1, buffer2))



if __name__ == "__main__":

    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"
    answer = "746865206b696420646f6e277420706c6179"

    # Convert a, b to bytes strings

    a = bytes.fromhex(a)
    b = bytes.fromhex(b)
    

    print("Does the XOR hex string match: ",answer == xor(a, b).hex())

    

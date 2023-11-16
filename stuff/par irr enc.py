import base64
import string
import binascii

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

"""
# do it 15 times plz
encrypted = "Encode as if there's no tomorrow: " + FLAG
for _ in range(15):
    # encode the FLAG in the 4 different ways, always the same order
    b64_encrypted = base64encode(encrypted)
    rot13_encrypted = ROTencode(b64_encrypted, 13)
    b32_encrypted = base32encode(rot13_encrypted)
    encrypted = ROTencode(b32_encrypted, 3)
"""

# We need to perform the steps in reverse
# I'll need some helper functions! 

def XORdecode(message, KEY="c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored
# XOR is symmetric, can just reuse the old function, key is included :)
# I just renamed it from Encode to Decode :P

# i'm very new to python, the encoding and then decoding in ascii confused me a bit. 
def base64decode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64decode(message_bytes)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

def base32decode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32decode(message_bytes)
    b32_message = b32_bytes.decode('ascii')
    return b32_message

def ROTencode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i+pos)%LEN]
    return rot13_enc

with open("encrypted_flag.txt", "r") as f:
    hex_dec=binascii.unhexlify(f.read()).decode()
    
xor_dec = XORdecode(hex_dec)

# now i just need to reverse the steps in the for loop!
for i in range(15):
    rot3_dec = ROTencode(xor_dec, -3)
    b32_dec = base32decode(rot3_dec)
    rot13_dec = ROTencode(b32_dec, -13)
    xor_dec = base64decode(rot13_dec)

print(xor_dec)
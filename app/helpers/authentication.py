from Crypto.Cipher import AES
import base64
import os

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: (s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING).encode('utf-8')

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: str(c.decrypt(base64.b64decode(e)), 'utf-8').rstrip(PADDING)

# generate a random secret key
secret = b'\xe3\xdd\x00s+\xfc\xe0\x0ee\x1e\xbb\xaeGIs\xf4\xf3\x9a\xe8IkkoZ{f}T\n.\xf1\x08'

# create a cipher object using the random secret
cipher = AES.new(secret, AES.MODE_ECB)

# encode a string
def encryption(password, encode=False):
    encoded = EncodeAES(cipher, password)
    decoded = DecodeAES(cipher, encoded)
    if encode:
        return encoded
    else:
        return decoded
        

# decode the encoded string
    
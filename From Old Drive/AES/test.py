__author__ = 'yousefhamza'

from Crypto.Util.number import *
import unittest
from aes import AES


key        = b'\xc3,\\\xa6\xb5\x80^\x0c\xdb\x8d\xa5z*\xb6\xfe\\'
ciphertext = b'\xd1O\x14j\xa4+O\xb6\xa1\xc4\x08B)\x8f\x12\xdd'
print(hex(bytes_to_long(ciphertext)))
print(hex(bytes_to_long(key)))



class AES_TEST(unittest.TestCase):
    def setUp(self):
        master_key = 0xc32c5ca6b5805e0cdb8da57a2ab6fe5c
        self.AES = AES(master_key)

    def test_decryption(self):
        ciphertext = 0xd14f146aa42b4fb6a1c40842298f12dd
        decrypted = self.AES.decrypt(ciphertext)
        print(long_to_bytes(decrypted))

if __name__ == '__main__':
    unittest.main()

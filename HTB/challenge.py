#!/usr/bin/python3
import os
from pwn import xor
# flag = open('C:\\repos\PythonZad\HTB\\flag.txt', 'r').read().strip().encode()
# 134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9
flag = "134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9".strip().encode()
mytext = "T".strip().encode()
# print(flag)
# HTB{ == 13 4a f6 e1 
#         48 54 42 7b
#         H  T  B  {
#         5b 1e b4 7b       #key (?) in decimal --> 1528738939

class XOR:
    def __init__(self):
        self.key = bytes(2)
        # self.key = bytes.fromhex("5b1eb47b")
    def encrypt(self, data: bytes) -> bytes:
        xored = b''
        for i in range(len(data)):
            xored += bytes([data[i] ^ self.key[i % len(self.key)]])
        return xored

    def decrypt(self, data: bytes) -> bytes:
        return self.encrypt(data)

def main():
    global flag
    crypto = XOR()
    print (crypto.key)
    secret = bin(crypto.encrypt(mytext).hex())
    print ('Flag encrypt:', crypto.encrypt(mytext).hex())
    print ('Flag decrypt:', crypto.decrypt(secret))

if __name__ == '__main__':
    # print(xor("5b1eb47b"))
    main()

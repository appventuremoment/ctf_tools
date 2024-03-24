# I'm Xorry

import os

flag="Redacted"
key=os.urandom(8)

def encrypt(flag,key):
    key_long=(key * (len(flag)//len(key)))[:len(flag)]
    encrypted = list(map(lambda p, k: chr(p^k), flag, key_long))

    return encrypted

def encrypt2(flag,key):
    key_long=(key * (len(flag)//len(key)))[:len(flag)]
    encrypted = list(map(lambda p, k: str(p^ord(k)) + ', ', flag, key_long))

    return encrypted


flag = [int('5b743e0c660d5d193d5d655220610d084c5d7848355a4d14'[i:i+2], 16) for i in range(0, len('5b743e0c660d5d193d5d655220610d084c5d7848355a4d14'), 2)]

lst = [12, 60, 12, 60, 84, 57, 38]


for i in range(256):
    try:
        result="".join(encrypt(flag, lst + [i]))
        print(f'Output: {result}') #Cough cough Output: 5b743e0c660d5d193d5d655220610d084c5d7848355a4d14
    except:
        test = 1
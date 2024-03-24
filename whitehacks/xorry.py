import os

flag="RedactedRRRRRRRRRRRRR"
key=os.urandom(8)

def encrypt(flag,key):
    key_long=(key * (len(flag)//len(key)))[:len(flag)]
    print(list(map(lambda p, k: str(k) + ' ', flag, key_long)))
    encrypted=result = list(map(lambda p, k: str(ord(p) ^ k) + ' ', flag, key_long))

    return encrypted
result="".join(encrypt(flag,key))
print(f'Output: {result}') #Cough cough Output: 5b743e0c660d5d193d5d655220610d084c5d7848355a4d14

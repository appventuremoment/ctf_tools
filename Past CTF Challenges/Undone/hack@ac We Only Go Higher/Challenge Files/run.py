import random
from Crypto.Util.number import bytes_to_long

with open('flag.txt', 'rb') as f:
    flag = f.read().strip()

secret_number = bytes_to_long(flag)

MAX_DIGITS = 80
assert secret_number < pow(10, MAX_DIGITS+1)

rand_seq_1 = [random.randint(1, 2) for _ in range(MAX_DIGITS)]
rand_seq_2 = [random.randint(19, 22) for _ in range(MAX_DIGITS)]

def encrypt(msg :int):
    msg = str(msg)
    enc = 0
    multiplier = 1
    for i in range(len(msg)):
        enc += int(msg[len(msg) - i - 1]) * multiplier * rand_seq_1[i]
        multiplier *= rand_seq_2[i]
    
    return enc

def verify(query :str):
    if query.isdigit():
        query = int(query)
        if query < pow(10, MAX_DIGITS+1) and query > 0:
            return query
    return -1

def main():   
    print("Encrypted Secret: ", encrypt(secret_number))
    print('')

    tries = 300
    while tries > 0:
        query = input("Enter a positive base 10 number to encrypt: ")
        query_processed = verify(query)

        if (query_processed != -1):
            query_enc = encrypt(query_processed)
            print(f"Here you go:\n{query_enc}")
            if (query_processed ==  secret_number):
                print("\nYou did it!")
                break
        else:
            print("Thats not a valid number!")
        
        tries -= 1
        print(f"Attempts left: {tries}\n")

    print("Goodbye")

main()
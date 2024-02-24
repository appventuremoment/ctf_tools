import random
import math

def xor(x, y):
    return [a^b for a, b in zip(x, y)]

def isSquare(x :int):
    return math.sqrt(x).is_integer()

def verify(x :int): # What am I?
    if x <= 0:
        return False
    
    y = x**2 - 1
    if y % 3 != 0:
        return False
    
    return isSquare(y // 3)

def get_input(n :int):
    print(f"Give me {n} numbers, space separated:")
    
    numbers = str(input()).strip().split()
    if len(numbers) != n:
        print(f'\nExpected {n} numbers, recieved {len(numbers)} numbers!')
        return 'error'
    
    userinput = []
    for number in numbers:
        if not number.isdigit():
            print(f'\n{number} is not a number!')
            return 'error'
        
        number = int(number)
        
        if verify(number):
            userinput.append(number)
        else:
            print(f'\nYour number {number} does not pass verification!')
            return 'error' 
    
    return userinput    

def get_key(n :int):
    key = []
    for _ in range(n):
        key.append(random.randint(0, 64))
        
    return key

def main():
    with open('flag.txt', 'r') as f:
        flag = f.read().strip()
    
    secret = []
    for c in flag:
        secret.append(ord(c))
    n = len(secret)
    
    key = get_key(n)
    print("Key is:")
    for i in key:
        print(i, end=' ')
    print('\n')
    
    userinput = get_input(n)
    if userinput == 'error':
        return
    
    s = []
    for number in userinput:
        s.append(math.floor(math.log(number, 10))) # What am I doing?
        
    if (s == key):
        response = xor(s, xor(key, secret))
        print("\nYou passed! Is this correct though...")
        print(response)
    else:
        print("\nI didn't get what I wanted :(")
    
if __name__ == "__main__":
    main()
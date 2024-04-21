def specStr(n):
    if n % 2 == 1: print('NO')
    else: 
        print('YES')
        print(('AAB' * (n // 2))[:-1])

for _ in range(int(input())):
    specStr(int(input()))
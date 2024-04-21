for _ in range(int(input())):
    n, k = list(map(int, input().split(' ')))
    if n == k: print(('1 ' * n)[:-1])
    elif k == 1: print(' '.join([str(x + 1) for x in range(n)]))
    else: print(-1)
for i in range(int(input())):
    n, one, two = list(map(int, input().split(' ')))
    if one * 2 < two:
        print(n * one)
    else:
        print(((n // 2) * two + (n % 2) * one))
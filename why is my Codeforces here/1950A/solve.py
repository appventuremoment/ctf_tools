for i in range(int(input())):
    a, b, c = list(map(int, input().split(' ')))
    if a < b:
        if b < c:
            print('STAIR')
        elif b > c:
            print('PEAK')
        else:
            print('NONE')
    else:
        print('NONE')
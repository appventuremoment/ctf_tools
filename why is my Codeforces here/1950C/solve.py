for i in range(int(input())):
    H, M = list(map(int, input().split(':')))
    if H == 0:
        print('12:' + ('0' * (2 - len(str(M))) + str(M) + ' AM'))
    elif H == 12:
        print('12:' + ('0' * (2 - len(str(M))) + str(M) + ' PM'))
    else:
        if H // 12 == 1:
            print(('0' * (2 - len(str(H - 12)))) + str(H - 12) + ':' + ('0' * (2 - len(str(M)))) + str(M) + ' PM')
        else:
             print(('0' * (2 - len(str(H)))) + str(H) + ":" + ('0' * (2 - len(str(M)))) + str(M) + ' AM')
def checkTents(I, E, U):
    if E % 3 + U < 3 and E % 3 != 0:
        return -1
    else:
        return I + E // 3 + (E % 3 + U) // 3 + ((E % 3 + U) % 3 != 0 and 1 or 0)

for _ in range(int(input())):
    I, E, U = list(map(int, input().split(' ')))
    print(checkTents(I, E, U))
def XORlist(inp):
    ret = 0
    for i in inp:
        ret ^= i
    return ret

def ListToString(inp):
    ret = ""
    for x in inp:
        ret += str(x) + " "
    return ret[:-1]

def CompareXORList(A, B):
    for x in A:
        for y in B:
            if XORlist(x) == XORlist(y):
                 print(ListToString(x)) 
                 print(ListToString(y))
                 return


from itertools import *
for i in range(int(input())):
    n, k = list(map(int, input().split(' ')))
    lst = list(map(int, input().split(' ')))
    lista = list(map(list, combinations(lst[:n], 2 * k)))
    listb = list(map(list, combinations(lst[n:], 2 * k)))
    CompareXORList(lista, listb)
for _ in range(int(input())):
    leng = int(input())
    arr = sorted(list(map(int, input().split(' '))))
    if leng <= 2: print(1)
    else:
        left, median, right = arr[leng // 2 - 1], arr[leng // 2], arr[leng // 2 + 1]
        print(min(median - left + 1, right - median + 1))
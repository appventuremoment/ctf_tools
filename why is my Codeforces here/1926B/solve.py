for i in range(int(input())):
    temp = []
    for x in range(int(input())):
        temp.append(input().count('1'))
    if temp.count(max(temp)) == max(temp):
        print("SQUARE")
    else:
        print("TRIANGLE")
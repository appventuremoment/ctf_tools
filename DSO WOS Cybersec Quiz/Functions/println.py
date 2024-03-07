def printlnX(x):
    printstr = ""
    for i in range(0, x - 1):
        printstr += str(i) + ", "
    printstr += str(x - 1)
    print(printstr)

printlnX(3)
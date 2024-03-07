def printlnX(x):
    printstr = ""
    for i in range(0, x - 1):
        printstr += str(i) + ", "
    printstr += str(x - 1)
    return printstr

def printMatrixX(x):
    printstr = ""
    for i in range(0, x - 1):
        printstr += printlnX(x)
        printstr += "\n"
    printstr += printlnX(x)
    print(printstr)

printMatrixX(4)
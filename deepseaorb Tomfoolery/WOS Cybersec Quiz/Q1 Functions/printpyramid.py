def printlnX(x):
    printstr = ""
    for i in range(0, x - 1):
        printstr += str(i) + ", "
    printstr += str(x - 1)
    return printstr

def printPyramid(x):
    printstr = ""
    for i in range(0, x - 1, 1):
        printstr += printlnX(i + 1)
        printstr += "\n"
    
    for i in range(x - 1, 0, -1):
        printstr += printlnX(i + 1)
        printstr += "\n"
    printstr += printlnX(1)
    print(printstr)

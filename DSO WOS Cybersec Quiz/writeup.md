# DSO Cybersec Module Quiz

## Question 1
The function *printlnX* is defined as:
```
printlnX(int x) {
    for(int i = 0; i < x; i++)
        printNumStr (i, ", ");
}
```

### a. 
```
printlnX(int x) {
    for(int i = 0; i < (x - 1); i++)
        printNumStr (i, ", ");
    printNumStr(x - 1); 
}
```

### b. 

Assuming we are able to call *printlnX(int x)* from part a
```
printMatrixX(int x) {
    for(int i = 0; i < (x - 1); i++)
        printlnX(x);
        printNumStr ("\n");
    printlnX(x);
}
```

If not
```
printMatrixX(int x) {
    for(int i = 0; i < (x - 1); i++)
        for(int j = 0; i < (x - 1); j++)
            printNumStr (j, ", ");
        printNumStr(x - 1, "\n"); 
    
    for(int j = 0; i < (x - 1); j++)
        printNumStr (j, ", ");
    printNumStr(x - 1); 
}
```

### c.
Assuming we are able to call *printlnX(int x)* from part a
```
printPyramid(int x) {
    for(int i = 0; i < (x - 1); i++)
        printlnX(i);
        printNumStr ("\n");

    for(int i = x - 1; i < (x - 1); i++)
        printlnX(i);
        printNumStr ("\n");
}
```

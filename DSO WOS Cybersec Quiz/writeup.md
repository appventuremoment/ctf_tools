# DSO Cybersec Module Quiz

## Question 1
The function *printlnX* is defined as:
```
printlnX(int x) {
    for(int i = 0; i < x; i++)
        printNumStr (i, ", ");
}
```

Assumption: printNumStr(int x, str y) takes in a number and a string, concatenates them and prints them, so printStr(str x) will print the string given and printNum(int x) will print the number given

### (a) 
```
printlnX(int x) {
    for(int i = 0; i < (x - 1); i++)
        printNumStr(i, ", ");
    printNum(x - 1); 
}
```

### (b) 

Assuming we are able to call *printlnX(int x)* from part (a)
```
printMatrixX(int x) {
    for(int i = 0; i < (x - 1); i++)
        printlnX(x);
        printStr("\n");
    printlnX(x);
}
```

If not
```
printMatrixX(int x) {
    for(int i = 0; i < (x - 1); i++)
        for(int j = 0; j < (x - 1); j++)
            printNumStr(j, ", ");
        printNumStr(x - 1, "\n"); 
    
    for(int j = 0; j < (x - 1); j++)
        printNumStr(j, ", ");
    printNum(x - 1); 
}
```

### (c)
Assuming we are able to call *printlnX(int x)* from part (a)
```
printPyramid(int x) {
    for(int i = 0; i < (x - 1); i++)
        printlnX(i + 1);
        printStr("\n");

    for(int i = x - 1; i < 0; i--)
        printlnX(i + 1);
        printStr("\n");
    printlnX(1);
}
```

If not
```
printPyramid(int x) {
    for(int i = 0; i < (x - 1); i++)
        for(int j = 0; j < (i - 1); j++)
            printNumStr(j, ", ");
        printNumStr(i - 1, "\n"); 

    for(int i = x - 1; i < 0; i--)
        for(int j = 0; j < (i - 1); j++)
            printNumStr(j, ", ");
        printNumStr(i - 1, "\n");
    printNum(0);
}
```

### (d)
Assuming we are able to call *printPyramid(int x)* from part (c)
```
printRidge(list x) {
    for(int i = 0; i < length(x); i++)
        for(int i = 0; i < (item(x, i) - 1); i++)
            for(int j = 0; j < (i - 1); j++)
                printNumStr(j, ", ");
            printNumStr(i - 1, "\n"); 

        for(int i = item(x, i) - 1; i < 0; i--)
            for(int j = 0; j < (i - 1); j++)
                printNumStr(j, ", ");
            printNumStr(i - 1, "\n");
        printNum(0);
}
```

## Question 2

Assume that your computer only has two built in unary operators, ++ and --.

```
add 0 y = y
add x 0 = x
add x y
    | (x < y) = add y x
    | otherwise = add (x--) (y++)
```

### (a)
Explain why it does not terminate and Try (5, 3)

### (b)(i)
Perhaps to check whether it is an integer
Modulus Function?

### (b)(ii)
define function and describe why better

### (b)(iii)
show example on 17 13

### (c)
modify code to take in negative numbers


## Question 3

### (a)(i)
memory location

### (a)(ii)
memory location

### (a)(iii)
set value of memory location between 100 and 200

### (b)(i)
modify to make it 4 * V1 + 10

### (b)(ii)
modify it to make it V1 * V2

### (b)(iii)
show example with large V1 and small V2
Crypto Challenge

Phew! This one is an actual challenge and not a silly one. Inspecting the file we see that firstly we are given a key in the form of 50 numbers. The server then wants a response of 50 numbers separated by spaces, where the common logarithm of each number is equals to the corresponding number in the given key. 
```
    for number in userinput:
        s.append(math.floor(math.log(number, 10))) # What am I doing?
        
    if (s == key):
    #code here giving response
```


Scrolling up, we see that they also want the numbers in a specific form. All input numbers squared minus one should be divisible by 3, and the integer division of each number by 3 should be a square number.
```
def isSquare(x :int):
    return math.sqrt(x).is_integer()

def verify(x :int): # What am I?
    if x <= 0:
        return False
    
    y = x**2 - 1
    if y % 3 != 0:
        return False
    
    return isSquare(y // 3)
```

Now, we make a script to look for a list of numbers corresponding to 0-65 such that they meet all the requirements. 
```
#Gettting initial list of corresponding nunmbers
listofnum = []
for i in range(65):
    for x in range(10 ** i, 10 ** (i + 1)):
        if verify(x):
            listofnum.append(x)
            break
print('Initial list:\n', listofnum, '\n')
```

However, printing out the list gives us a rather perculiar list. Numbers from 18 digits and above are all 10 ** i, where i is their respective indices. How strange! We will keep this in mind for later. 

Now with list in hand, we run the script attempting to get the flag. However, running the script gives us an error
```
Your number {number} does not pass verification!
```
for specific numbers? How?

Adding in a check, we find out that some of the common logarithms of numbers do not equal their indicies. How is that possible? 
Making another script, we check for the indices where the common logarithms do not match their indices. 
```
index = []
for i in range(65):
    if math.floor(math.log(listofnum[i], 10)) != i:
        index.append(i)
print('Index of non-matching numbers:\n', index, '\n')
#index = [18, 21, 23, 24, 26, 27, 29, 30, 31, 33, 36, 39, 42, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 62, 63]
```
This gives us a list of numbers all above 10**17. That means they are all in the form of 10\*\*i. How is that possible?? log_10(10 \*\* x) should always return x. Now, while I have no clue why that happens, I do think that it may have something to do with floating points in python being inaccurate.




We now want to find replacement numbers for the numbers that have discrepancies between their powers and their common logarithms. But wait! Remember how all the numbers were 10**i? I realised right then that it was likely that any number would pass the test for being a square root. Testing that in another file (pymathlib.mp4), we find that the square root of numbers above a certain threshold are all evaluated as integers using the code
```
math.sqrt(number).is_integer()
``` 

Knowing that, we start by iterating through 10 ** i to 10 ** (i + 1) in intervals one magnitude lower.
```
replacements = []
for i in index:
    for x in range(10 ** i, 10 ** (i + 1), 10 ** (i - 1)):
        if verify(x):
            if math.floor(math.log(x, 10)) == i:
                replacements.append(x)
                break
        break
print('Replacement numbers for non-matching numbers:\n', replacements, '\n')
```
We then replace the wrong numbers in our already existing list with the new set of numbers and indices we have.
``` 
for x in range(len(replacements)):
    listofnum[index[x]] = replacements[x]

print('Final list of numbers from 0 to 64:\n', listofnum)
```

Finally we can rerun the code with the new list to get 
```
#You passed! Is this correct though...
# [65, 67, 83, 73, 123, 99, 48, 78, 103, 114, 65, 116, 53, 95, 117, 95, 77, 97, 53, 84, 51, 82, 101, 68, 95, 84, 72, 101, 95, 112, 51, 108, 49, 95, 101, 113, 85, 97, 116, 49, 48, 78, 33, 95, 102, 106, 50, 51, 100, 125]
```
which we then convert from integer to char using ord() to get the flag ACSI{c0NgrAt5_u_Ma5T3ReD_THe_p3l1_eqUat10N!_fj23d}
Looking at thge flag, it the intended solve was to use Pell's equation to find the corresponding numbers, but due to the several issues of the math library, we were able to come up with our own solution.


All files, both challenges and solutions are in their respective folders.

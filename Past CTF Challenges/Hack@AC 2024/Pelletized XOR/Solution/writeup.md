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
test
```
Your number {number} does not pass verification!')

ACSI{c0NgrAt5_u_Ma5T3ReD_THe_p3l1_eqUat10N!_fj23d}
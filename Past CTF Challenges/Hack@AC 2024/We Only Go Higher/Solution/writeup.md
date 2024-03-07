Crypto Challenge

This challenge was considered the hardest of all in this category. Based on the code below:

![nice try](https://github.com/appventuremoment/ctf_tools/blob/main/Past%20CTF%20Challenges/Hack%40AC%202024/We%20Only%20Go%20Higher/Solution/image.png)

We can tell that each number of the plaintext converted from bytes to long has been multiplied with multi and either 1 or 2 before being added to the output. Multiplier is increased with every iteration of the numbers in the plaintext, by a 19-22 fold based on the list.

It gives you 300 tries to input your plaintext, such that it matches the encrypted plaintext they output, after it has been encrypted in the same way. From this, we have 2 available options to solve this challenge. 

The first and intended solution is to realise that since they are encrypted the same way, a larger plaintext results in a larger ciphertext. This means we can binary search our way until we get the answer. The code is implemented in solution.py

The other way, which was done by @azazo is to realise that you can encrypt 10**i such that each i corresponds to rand_seq_1[i] * rand_seq_2[i], and since we know the ranges of rand_seq_1 and rand_seq_2, we can obtain the both lists. For example, if we entered in 10 ** 2 (100), and got back 3800, we can divide it by 10 ** 2 and check whether 38 / 2 is in the range 19 - 22, if it is, rand_seq_2[2] is 2, else it is 1.

After getting the whole list, we input an equation from x_i for x_0 to x_79, standing for each index of the plaintext into z3 multiplied by each corresponding rand_seq_1[i] and rand_seq_2[i] equating to the encrypted plaintext the server gave. From there, we find each x which corresponds to each digit of the plaintext in number form, reversed. Reversing it gives us the correct number.


Converting both of the numbers using long_to_bytes gives us the flag ACSI{bSTa_15_f4St_eN0Ugh_yAY}

Rev Challenge

Looking at the files, we see that the flag has been changed from ASCII characters to their corresponding codes in hexadecimal. We know that ASCII characters for alphabets are below 128 so they are 2 digits each. Hence, we split up the string every 2 digits.

We see that for the first character, nothing special is added but for the rest of the characeters, the even ones have 15 added to them and the odd ones have 15 subtracted from them (15 in decimal). Therefore, we simply copy the same format and reverse (addition substituted for subtraction and vice versa).
Very simple challenge. 

This gives us ACSI{b4ckw@rds_stuck_1m
Knowing the flag format, I assume that the flag would beACSI{b4ckw@rds_stuck_1m}. However, for whatever reason, I could not submit the flag so I had to get my teammate to submit it, which is kind of odd. Man.

Why could I not submit/10
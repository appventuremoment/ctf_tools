Rev Challenge

Looking at the files, we see that the flag has been changed from ASCII characters to their corresponding codes in hexadecimal. We know that ASCII characters for alphabets are below 128 so they are 2 digits each. Hence, we split up the string every 2 digits.

We see that for the first character, nothing special is added but for the rest of the characeters, the even ones have 15 added to them and the odd ones have 15 subtracted from them (15 in decimal). Therefore, we simply copy the same format and reverse (addition substituted for subtraction and vice versa).

This gives us the flagACSI{b4ckw@rds_stuck_1m_h3Lp}
Very simple challenge. 

However, during the competition itself, I somehow managed to delete part of the output file such that the flag I got was ACSI{b4ckw@rds_stuck_1m and I just assumed they forgot to add the other curly brace. I never thought about the possibility of me accidentally deleting parts of the output and a teammate had to run the code and submit for me.

Why could I not submit/10
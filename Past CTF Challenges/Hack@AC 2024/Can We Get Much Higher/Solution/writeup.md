Crypto Challenge

At first I thought of the small exponent attack for whatever reason, which is entirely wrong since the exponent was HUGE. I took quite a while trying to find something that could find the nth root of c, but it was not possible. 

Then I realised that this was the large exponent vulnerabilities (no way right it was even mentioned in the challenge description). Since the public exponent is very large, it means that the private exponent must be very small. There are specific attacks for this such as the Wiener's attack and the Boneh Durfee attack.

From this, using https://github.com/orisano/owiener, we find the private exponent and decerypt it normally to get the flag ACSI{d1d_you_use_w3iners_att4ck......https://youtu.be/gWo12TtN9Kk}

THE ONE PIECE IS REAL!/10


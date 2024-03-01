Crypto Challenge

Based on the challenge descrption, we are hinted at the fact that the file we have has been XOR'd.

I first tried to XOR the text with mice or fish but it did not work. After that, I realised the cyberchef had a way to brute force the characters. Hence, I entered the known part of the plaintext, which is PNG (the file header).

![nice try]()

This gave us the key of 02 in hex. We then input it into the XOR function on cyberchef to get the result:

![nice try]()

Downloading the output gives us:

![nice try]()

which has the flag written in the image ACSI{HaxX0r_C4+}

cat/10
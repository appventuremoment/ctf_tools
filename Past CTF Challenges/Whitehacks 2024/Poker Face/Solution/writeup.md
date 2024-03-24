# Crypto Challenge

The challenge greets with an image

![nice try](Poker_Face.png)

with no other explanation. Since this is a crypto challenge, it would not make sense to run any of the forensics tools on the image. Instead we recognise that this could be a cipher. Searching it up online, we find that it could be the solitare cipher https://en.wikipedia.org/wiki/Solitaire_(cipher). Unfortunately, nothing useful was found from this so it cannot be the case.

We then try to see if the cards each represent a letter which has been encrypted, since we see a few repeating ones.

i love caeser salad

Replacing each unique card with a unique letter gives us a_bcde_fgehei_jckcl. Running this through multiple solvers gives us nothing. We then realised that a deck of cards is 52 cards, twice of the alphabet so it must mean that capital letters are included.

Referencing this image, after sorting them in alphabetical order of suits and moving the ace to the front.

![nice try](image.png)


First, we attempt to have suit be half the letters, so from top to bottom it is

abcdefghijklm
nopqrstuvqxyz
ABCDEFGHIJKLM
NOPQRSTUVWXYZ

We run it through the usual decoders and it does not work. Next we try alternating letters that being

AaBbCcDdEeFfG

for the first line and so on.

Referencing this

![nice try](image2.png)

This would give us U_Xahq_Omqemd_Emxmp, which we can see matches the casing for titles. Putting this through https://www.quipqiup.com 

![nice try](image3.png)

we find the phrase I_Love_Caesar_Salad from the phrases, which we then wrap in the flag format to get obtain WH2024{I_Love_Caesar_Salad}. Sadly this was already solved when I started so I attempted this after the CTF ended. Only our team solved this surprisingly. 

0/10 bridge is a terrible game and the only bridges that will be burning are the ones you have with your friends.

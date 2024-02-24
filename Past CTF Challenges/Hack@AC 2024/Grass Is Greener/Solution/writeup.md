Forensics Challenge

So we have an image, but attempting to open it gives us problems. Using file image.png on lets us know that it is a data file? This is weird since this clearly should be an image, right? Using a hex editor we find that the file header it @NG instead of PNG (thank god is not the whole file header gone). Correcting it allows us to open the file. Now, all that is left is to do the usual forensics things.

Putting it into aperisolve.com gives us this
![nice try](https://github.com/appventuremoment/ctf_tools/blob/main/Past%20CTF%20Challenges/Hack%40AC%202024/Grass%20Is%20Greener/Solution/image.png)

This gives us the flag ACSI{t0uch_gr@55}
Rev Challenge

We are given an ELF file in a zip. Decompiling the file using IDA Pro gives us a lot of code, but inspecting it closely we see a function called EncryptWord as seen in the image here:

![nice try](link)

This tells us that the word has been encrypted with a substituition cipher of sorts, and replacing each unique number with a unique character (or using the replace.py script) gives us FKEL{WHFM_HNKJUTQLCN_JLT}, and since we know ACSI is not a real word, we input the inside of the flag into https://quipqiup.com to see:

![nice try](link)

Therefore, the flag was either "weak encryption rip" or "self encryption rip". Since the former is more likely, we will be trying that as the flag. Since we saw that the flag was converted to all uppercase in the decompiled code, we get the flag ASCSI{WEAK_ENCRYPTION_RIP}
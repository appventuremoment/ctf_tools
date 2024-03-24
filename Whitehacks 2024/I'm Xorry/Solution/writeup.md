Crypto Challenge

Very simple XOR challenge. From this we see the bytes of the key is repeated to match the length of the flag. Key is XOR'd with flag.
We know plaintext starts with WH2024{. XORing it with the ciphertext we get the first 7 bytes of the key. Now we bruteforce the last byte and search for the flag with } as the last character.

Really simple, don't know why there are only 10 solves.

Flag: WH2024{p1aintX+a@attack}

Never again/10
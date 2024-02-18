So inspecting this program we find out a few things:
1. The program wants us to guess random numbers 500 times consecutively for the flag
2. We have 5000 guesses before we get kicked out of the server
3. The seed is random, or so it should have been, 
4. except it was messed up and instead the seed was the time of the server booting up and running that file times 10

In the actual CTF, we would connect to the server and generate the first number from the python random library +- 1000ms from the time of connection as the seed, until the number generated is deemed correct by the server.
From there, we know the time that the server used as the seed and iterate through the rest of the code to guess the rest of the numbers and input into the server for the flag.

However since at the time of writing, the servers are already down, we shall be changing the code a bit and running the files locally.
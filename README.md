# CTF Tools
Just a list of CTF Tools for my own use

![nice try](https://github.com/appeventuremoment/ctf_tools/blob/main/this%20cannnot%20continue.jpg)

For python 2 if you input variable name as it check if it is a variable it will allow it

```
r^n mod n^2 mod n
r < n
(r mod n)^n mod n
```

Stuff to readup:
- https://github.com/Lag-and-Crash/2024/tree/main/challenges
- https://bitsdeep.com/posts/analysis-of-the-roca-vulnerability/
- https://mathcrypto.wordpress.com/2014/11/11/probable-primes-and-pseudoprimes/
- https://nusgreyhats.org/posts/writeups/ductf-2023-encrypted-mail/

```py
t = int(time.time()*1000)

for i in range(5):
    p.recvuntil(b"card is ")
    card = eval(p.recvline().decode("utf-8").strip())
    head.append(card)

for i in range(-1000, 1000):
    if shuffle(t+i)[:5] == head:
        p.sendline(str(shuffle(t+i)).encode("utf-8"))
        break
```

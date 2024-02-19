Web Challenge GRRRRRRRR

So I found another challenge where the original site is down and the challenge description is not included, but based on the pho file given, it appears to be a website where the URL parameters are the input to get the flag. 

We can use https://www.programiz.com/php/online-compiler/ to run it online.


Now for the first part we see 

```php strcmp($inputsecret, $secret) != 0```

where the inputsecret parameter is compared to the secret using strcmp. From this writeup https://ctftime.org/writeup/19385, we know that strcmp has some flaws and hence we can input an array such that strcmp returns NULL, and since it is a loose comparison it will equate to 0.

For the second part, we see 

```php hash('sha1',$meaningoflife) != 42```

where they want the sha1 hash of the meaningoflife parameter to equal 42. That is normally impossible since sha1 hashes are usually a hex string with around 32 characters. However, from https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md we see that '123a' == 123 will equate to true due to the property of loose comparisons in php.

From here we just need to brute force a sha1 hash with 42 + anything character in [a, b, c, d, f] as the first 3 letters. e does not work since php will evaluate it as a scientific notation.  

From this, we find that 227 can be a possible input for meaningoflife.

This gives us the flag blahaj{REDACTED} because we don't actually have the site anymore.
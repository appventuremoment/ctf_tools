# Misc Challenge

When you connect to the server, you are greeted with the message:

```
# Welcome to the Polynomial Playground, where you'll embark on an exhilarating journey of polynomial creation! Get ready to flex your mathematical muscles as you craft intricate equations from a given set of roots. Are you up for the challenge?

# In this mind-bending adventure, your task is to construct polynomials using a set of provided roots. Armed with your mathematical prowess and creativity, you'll delve into the world of polynomial composition and unlock the secrets of equation crafting.

# From simple quadratics to complex higher-degree polynomials, each level presents a new set of roots waiting to be transformed into an elegant equation. But don't be fooled by the simplicity of the task; as you progress, the challenge will intensify, requiring you to employ strategic thinking and mathematical precision.

# How to Play:
# 1. You'll be given a set of `n` roots for each level.
# 2. Utilize your mathematical knowledge to construct a polynomial equation that has the provided roots. You can assume that repeated roots will be given as repeats.
# 3. Channel your creativity and problem-solving skills to craft elegant and efficient equations.
# 4. Submit your polynomial creations as a comma-separted list of `n+1` coefficients starting with the highest order (which should always be 1).

# Are you ready to unleash your inner mathematician and become a master polynomial architect? Prepare to explore the depths of equation construction, unlock the beauty of mathematical expression, and emerge victorious in the Polynomial Playground! 
```

The problems are given in the format of 
```
# Here's your first problem...
# --------------------
# Level 1:
# Roots: 615
# Present the coefficients of your amazing equation:
```

and for those with multiple roots, they are given separated with a single comma and no space (why?)
```
# --------------------
# Level 28:
# Roots: -811,995
# Present the coefficients of your amazing equation:
```

Simply connect to it and use numpy.polynomial to get the roots of the equation and send it back to the server.
We get the flag grey{l0oks_lik3_sOm3one_c4n_b3_a_po1ynomia1_w1z4rd}
FLAG = "\n_I6~\x03G(2^\x03g\x08\x12~\x03G(\x12~\x03g*'"

def xor(a, b):
    return "".join([chr(ord(i)^ord(j)) for i, j in zip(a, b)])

test = "gm2{M30"
while True:
    test = (b"g" + xor(FLAG, test).encode()).decode()
    print(test)

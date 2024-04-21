def XORNumStr(str1, str2): return ''.join(list(map(str, [int(a) ^ int(b) for a, b in zip(str1, str2)])))

print(XORNumStr(input(), input()))

# One liner
# print(''.join(list(map(str, [int(a) ^ int(b) for a, b in zip(input(), input())]))))
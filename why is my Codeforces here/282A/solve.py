out = 0
for _ in range(int(input())): out += ('+' in input() and 1 or -1)
print(out)
counter = []
for _ in range(int(input())): counter.append(input().split(' ').count('1') >= 2)
print(counter.count(True))
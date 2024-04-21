crew, rankings = {}, {'rat': 0, 'woman': 1, 'child': 1, 'man': 2, 'captain': 3}
for _ in range(int(input())):
    name, role = input().split(' ')
    crew[name] = rankings[role]

for out in list(dict(sorted(crew.items(), key = lambda x:x[1])).keys()): print(out)
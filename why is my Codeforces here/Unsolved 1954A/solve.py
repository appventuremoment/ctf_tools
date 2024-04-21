def checkColours(parts, colours, bob):
    if parts == 1 or colours == 1:
        return 'NO'
    else:
        ribcolours = {}
        for colour in range(colours): ribcolours[colour] = parts // colours
        for i in range(parts % colours): ribcolours[i] += 1
        if sum(ribcolours.values()) - max(ribcolours.values()) <= bob: return 'NO'
        else: return 'YES'

for _ in range(int(input())):
    parts, colours, bob = list(map(int, input().split(' ')))
    print(checkColours(parts, colours, bob))
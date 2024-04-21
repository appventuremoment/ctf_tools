def printCheckers(n, times):
    for y in range(n * times): print(''.join(y % (2 * times) < times and ['#' if x % (2 * times) < times else '.' for x in range(times * n)] or ['#' if x % (2 * times) >= times else '.' for x in range(times * n)]))

for i in range(int(input())): printCheckers(int(input()), 2)
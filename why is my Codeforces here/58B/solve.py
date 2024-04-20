def Factors(n):
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return factors

def findDenominations(n):
    factors = Factors(n)[::-1]
    denoms = [n]
    for factor in factors:
        test = [x % factor for x in denoms]
        if len(set(test)) == 1:
            denoms.append(factor)

    ret = ""
    for denom in denoms:
        ret += str(denom) + " " 
    return ret[:-1]

n = int(input())
print(findDenominations(n))
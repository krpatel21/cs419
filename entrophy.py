import math

def ent(p, n):
    pos = float(p) / (p+n)
    neg = float(n) / (p+n)
    return -1 * pos * math.log(pos, 2) - neg * math.log(neg, 2)

print ent(3,4)
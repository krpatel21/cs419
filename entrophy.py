import math

def ent(p, n):
    pos = float(p) / (p+n)
    neg = float(n) / (p+n)
    e = -info(pos) - info(neg)
    return e

def info(p):
    if p==0.0:
        return p
    else:
        return p*math.log(p,2)

def ent2( v1, v2, v3, v4):
    p1 = float(v1) / (v1+v2+v3+v4)
    p2 = float(v2) / (v1+v2+v3+v4)
    p3 = float(v3) / (v1+v2+v3+v4)
    p4 = float(v4) / (v1+v2+v3+v4)

    e = -info(p1) - info(p2) - info(p3) - info(p4)
    return e

def ent3( v1, v2, v3):
    t = v1 + v2 + v3
    p1 = float(v1) / (t)
    p2 = float(v2) / (t)
    p3 = float(v3) / (t)

    e = -info(p1) - info(p2) - info(p3) 
    return e

#
# def ent(v1, v2, v3, v4):
#     p1 = float(v1) / (v1+v2+v3+v4)
#     p2 = float(v2) / (v1+v2+v3+v4)
#     p3 = float(v3) / (v1+v2+v3+v4)
#     p4 = float(v4) / (v1+v2+v3+v4)
#
#     return - p1 * math.log(p1,2) \
#             -  p2 * math.log(p2,2) \
#             -  p3 * math.log(p3,2) \
#             -  p4 * math.log(p4,2)
#
# def ent(v1, v2, v3, v4):
#     p1 = float(v1) / (v1+v2+v3+v4)
#     p2 = float(v2) / (v1+v2+v3+v4)
#     p3 = float(v3) / (v1+v2+v3+v4)
#     p4 = float(v4) / (v1+v2+v3+v4)
#
#     return - p1 * math.log(p1,2) \
#             -  p2 * math.log(p2,2) \
#             -  p3 * math.log(p3,2) \
#             -  p4 * math.log(p4,2)

# print ent(2,3)

# print 0.94 - (float(5)/14*(0.97)+float(5)/14*(0.97))

# print ent(5, 1, 3, 1)
# print ent(1, 0, 2, 0) #urgent
# print ent(2, 0, 1, 1) # near
# print ent(2, 0, 1, 0) # none
#
# print ent(1,2)
# print ent(2,1)
#
# print (-1.0/2*math.log(1.0/2, 2)) - (1.0/4*math.log(1.0/4, 2)) -(1.0/4*math.log(1.0/4, 2))

print ent2(5, 1, 3, 1)
print ent2(1, 0, 2, 0)
print ent2(2, 0, 1, 1)
print ent2(2, 1, 0, 0)
print
print ent2(5, 0, 0, 0)
print ent2(0, 1, 3, 1)
print
print ent2(3, 1, 1, 1)
print ent2(2, 0, 2, 0)
print
print ent2(5, 1, 3, 1) - float(3)/10*ent2(1, 0, 2, 0) - float(4)/10 *ent2(2, 0, 1, 1) - float(3)/10 *ent2(2, 1, 0, 0)
print ent2(5, 1, 3, 1) - float(5)/10*ent2(5, 0, 0, 0)- float(5)/10* ent2(0, 1, 3, 1)
print ent2(5, 1, 3, 1) - float(5)/10* ent2(3, 1, 1, 1) - float(5)/10*  ent2(2, 0, 2, 0)
print
print ent3(1,3,1)
print ent3(0,2,0)
print ent3(0,1,1)
print ent3(1,0,0)
print ent3(1,3,1)- 2.0/5 * ent3(0,1,1)
print
print ent3(1,1,1)
print ent3(1,3,1) - 3.0/5 * ent3(1,1,1)

print ent3(1,1,1)
print ent3(1,1,1)

print
print ent(1,1)
print ent(1,0)
print ent(0,2)
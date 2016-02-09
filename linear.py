import math


def avg(l):
    s = sum(l) / float(len(l))
    return s


list = [3.45, 2.78, 2.52, 3.67, 3.24]


# print avg(list)

def std(list):
    n = len(list)
    a = avg(list)
    s = 0
    for v in list:
        s += (v - a) ** 2
    std = math.sqrt(float(s) / (n - 1))
    return std


print std(list)

list2 = [1232, 1070,1086,1287,1130]

print std(list2)

def r(list1, list2):
    std1 = std(list1)
    std2 = std(list2)
    s = 0
    a1 = avg(list1)
    a2 = avg(list2)
    n = len(list1)
    for x in range(0, len(list1)):
        # print list1[x]
        # print list2[x]
        s += (float(list1[x]-a1)/std1) *(float(list2[x]-a2)/std2)
    r = 1.0/(n-1) * s
    return r

def slope(list1, list2):
    s = r(list1,list2) * std(list2) / std(list1)
    return s

print slope(list, list2)

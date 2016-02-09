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




list2 = [1232, 1070,1086,1287,1130]



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

def slope(listx, listy):
    s = r(listy,listx) * std(listy) / std(listx)
    return s


def yint(avgx, avgy, slope):
    y = avgy - slope * avgx
    return y

m = slope(list, list2)
avgx = avg(list)
avgy = avg(list2)

print m
print yint(avgx, avgy, m)

nitrates = [50, 50, 100, 200, 400, 800, 1200, 1600, 2000, 2000]
absorbance = [7.0, 7.5, 12.8, 24.0, 47.0, 93.0, 138.0, 183.0, 230.0, 226.0]

stdn = std(nitrates)
stda = std(absorbance)

nav = avg(nitrates)
aav = avg(absorbance)

r1 = r(nitrates, absorbance)

m1 = slope(absorbance, nitrates)
m2 = slope(nitrates, absorbance)

avgn = avg(nitrates)
avga = avg(absorbance)

yintn = yint(avgn, avga, m2)
yinta = yint(avga, avgn, m1)

print m1, m2, r1, stdn, stda
print
print yintn, yinta

year = [1935, 1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980]
population = [32.1, 30.5, 24.4, 23.0, 19.1, 15.6, 12.4, 9.7, 8.9, 7.2]

avy = avg(year)
avp = avg(population)
print slope(population,year)
print yint(avp, avy, slope(population,year))

print slope(year,population)
print yint(avy, avp, slope(year,population))

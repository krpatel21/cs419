import math
import pylab

list = [3.45, 2.78, 2.52, 3.67, 3.24]
list2 = [1232, 1070,1086,1287,1130]

def mean(x):
    s = sum(x) / float(len(x))
    return s

# print avg(list)

def sd(x):
    n = len(x)
    a = mean(x)
    s = 0
    for v in x:
        s += (v - a) ** 2
    std = math.sqrt(float(s) / (n - 1))
    return std

def r(x, y):
    std1 = sd(x)
    std2 = sd(y)
    s = 0
    a1 = mean(x)
    a2 = mean(y)
    n = len(x)
    for i in range(0, len(x)):
        s += (float(x[i] - a1) / std1) * (float(y[i] - a2) / std2)
    r = 1.0/(n-1) * s
    return r

def slope(x, y):
    s = r(y, x) * sd(y) / sd(x)
    return s

def yint(avgx, avgy, slope):
    y = avgy - slope * avgx
    return y

def lm(x,y):
    slope = r(x, y) * sd(y) / sd(x)
    meanx = mean(x)
    meany = mean(y)
    yint = meany - slope * meanx
    return (yint, slope)

m = slope(list, list2)
avgx = mean(list)
avgy = mean(list2)

print m
print yint(avgx, avgy, m)
print lm(list,list2)

nitrates = [50, 50, 100, 200, 400, 800, 1200, 1600, 2000, 2000]
absorbance = [7.0, 7.5, 12.8, 24.0, 47.0, 93.0, 138.0, 183.0, 230.0, 226.0]

stdn = sd(nitrates)
stda = sd(absorbance)

nav = mean(nitrates)
aav = mean(absorbance)

r1 = r(nitrates, absorbance)

m1 = slope(absorbance, nitrates)
m2 = slope(nitrates, absorbance)

avgn = mean(nitrates)
avga = mean(absorbance)

yintn = yint(avgn, avga, m2)
yinta = yint(avga, avgn, m1)

print m1, m2, r1, stdn, stda
print
print lm(nitrates,absorbance)
print lm(absorbance,nitrates)
year = [1935, 1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980]
population = [32.1, 30.5, 24.4, 23.0, 19.1, 15.6, 12.4, 9.7, 8.9, 7.2]

avy = mean(year)
avp = mean(population)
print slope(population,year)
print yint(avp, avy, slope(population,year))

print slope(year,population)
print yint(avy, avp, slope(year,population))
print lm(population, year)
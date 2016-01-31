'''
    This file is an incomplete version of a decision tree in python. You have to fill out the
    the portions that have a TODO comment in them. 
'''
import collections,math,pprint,sys
import operator

# The following functions are utility functions to read the files
# and some are be useful for your homework. That is, they are called
# from within the functions you have to implement.

def file2list(fname):
    d = open(fname).read().split("\n")
    data = [instance.split(",") for instance in d if len(instance)>1]
    return data


def line2attribs(line,target):
    d = {}
    for i,val in enumerate(line):
        if i!=target:
            d[i]=val
    return d


def info(p):
    if p==0.0:
        return p
    else:
        return p*math.log(p,2)


def getSubsetsByValues(s,a):
    sv = {}
    for ex in s:
        sv[ex[a]] = sv.get(ex[a],[])
        sv[ex[a]].append(ex)
    return sv


def count_values(s,target):
    t = [x[target] for x in s] # t is a list with all the target values in s
    return collections.Counter(t) # count how many of each value there are


def most_common_value(s,target):
    counts = count_values(s,target)
    return counts.most_common()[0]

def entropy(s,target):
    '''
        s is the set of examples.
        target is the index of the target attribute
    '''
    r = count_values(s,target).values()

    p = r[0]
    if (len(r) == 1):
        n = 0
    else:
        n= r[1]
    t = p + n
    probp = float(p)/t
    probn = float(n)/t

    e = - info(probp) - info(probn)
    return e


def gain(s,a,target):
    '''
        s is the set of examples.
        a is the attribute index to look at
        target is the index of the target attribute in s
    '''
    totalE = entropy(s, 4)
    everything = count_values(s, 4).values()
    sub = getSubsetsByValues(s, target)
    d = everything[0] + everything[1]
    for s1 in sub:
        r = count_values(sub[s1],4).values()
        en = entropy(sub[s1] , 4)
        if len(r) == 2:
            n = r[0]+r[1]
        else:
            n = r[0]
        totalE -= float(n) /d * en
    return totalE

def getBestAttribute(s,attributes,target):
    gains = {}
    best_gain = 0
    for a in attributes:
        g = gain(s, attributes, a)
        gains.update({a:g})
        if g > best_gain:
            best_gain = g
    return max(gains.iteritems(), key=operator.itemgetter(1))[0]


def id3(examples,target,attributes): #look at page 56 of Mitchell's book
    '''
        examples is the set of examples WITHOUT the header row
        target is the index of the target attribute
        attributes is a dictionary where keys are attribute indices and values
            are attribute names
    '''
    root = {}
    if entropy(examples,target)==0.0: #if all examples are positive or negative
        return examples[0][target]    #return a single node
    if len(attributes)==0:     # if there are no more attributes to explore,
        return root            # return the root
    a = getBestAttribute(examples,attributes,target)
    root[attributes[a]]={}
    examples_by_val = getSubsetsByValues(examples,a)
    for v,ex_sv in examples_by_val.items(): # for each possible value v of a
        if not ex_sv:
           root[a]=most_common_value(examples,target)
        else:
           dic = removekey(attributes, a)
           root[attributes[a]][v] = id3(ex_sv,target,dic)

    return root
    
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def dtree(datafile):
    data = file2list(datafile)
    target = len(data[0])-1 #assume that the target attribute is the last one
    attributes = line2attribs(data[0],target) # get attribute names & indices from 1st line
    root = id3(data[1:],target,attributes) # put the ID3 tree in a root node
    pprint.pprint(root) #pprint = pretty print.

if __name__=='__main__': #this allows you to run this program from cmd line.
    fname = sys.argv[1]
    dtree(fname)



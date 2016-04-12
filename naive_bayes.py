import pprint
import random
import math

def file2list(fname):
    d = open(fname).read().split("\n")
    data = [instance.split(",") for instance in d if len(instance) > 1]
    return data


# pprint.pprint(file2list("car.data.txt"))
dataset = file2list("car.data.txt")


def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


splitRatio = 0.7
train, test = splitDataset(dataset, splitRatio)
print 'Split {0} rows into train with {1} and test with {2}'.format(len(dataset), train, test)


def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated


def attributes(dataset):
    separated_dict = {}
    attr_list = []
    for i in range(len(dataset[1]) - 1):
        separated_dict[i] = []
    for i in range(len(dataset)):
        vector = dataset[i]
        for j in range(len(vector) - 1):
            if (vector[j] not in separated_dict[j]):
                separated_dict[j].append(vector[j])
    return separated_dict


attribute_dict = (attributes(dataset))
print len(attribute_dict)
pprint.pprint(attribute_dict)
separated = separateByClass(train)

# pprint.pprint(separated)
keys = separated.keys()
# print('Separated instances: {0}').format(separated)

total = len(dataset)


def classifier_prior_probalities(keys, seperated):
    probabilities = {}
    for k in keys:
        probabilities[k] = len(separated[k]) / float(total), len(separated[k])
    return probabilities


cpp = classifier_prior_probalities(keys, separated)
print cpp


def frequency_table(seperated, attribute_dict, keys):
    data = separated
    freq = {}
    frequency = {}
    for k in keys:
        freq[k] = {}
        working_set = data[k]
        for i in range(len(attribute_dict)):
            frequency[i] = []
        for i in range(len(attribute_dict)):
            for j in range(len(attribute_dict[i])):
                frequency[i].append(0)
        for j in working_set:
            for i in range(len(attribute_dict)):
                counter = 0
                for l in attribute_dict[i]:
                    if j[i] == l:
                        frequency[i][counter] += 1
                    counter += 1
        freq[k].update(frequency)
    return freq


f = frequency_table(separated, attribute_dict, keys)

def likelyhood_table(f, keys, cpp):
    llist = {}
    for k in keys:
        llist[k] = {}
        for i in range(len(attribute_dict)):
            llist[k][i] = []
        for i in range(len(attribute_dict)):
            for j in range(len(attribute_dict[i])):
                llist[k][i].append(0)
        tup = cpp[k]
        working_list = llist[k]
        for i in f[k]:
            for j in f[k][i]:
                ind =  f[k][i].index(j)
                working_list[i][ind] = j/float(tup[1])
    return llist

l = likelyhood_table(f, keys, cpp)

pprint.pprint(l)

def calculateargmax(row, likelyhood_table, cpp, keys, attributes):
    argmax = row[len(row)-1]
    max_probability = 0
    fp = 0
    for k in keys:
        probabilities = 1
        for i in range(len(row) - 1):
            tup = cpp[k]
            ptable = likelyhood_table[k]
            ind = int(attribute_dict[i].index(row[i]))
            plist= ptable[i]
            if plist[ind] != 0 or plist[ind] != 0.0:
                probabilities *= plist[ind]
            else:
                probabilities *= 0.00001
            if i == 5:
                fp = probabilities * tup[0]
            if (fp > max_probability):
                max_probability = fp
                argmax = k
    return argmax


def test_data(test, likelyhood_table, cpp, keys, attributes):
    correct = 0
    incorrect = 0
    data = test
    for i in data:
        argmax = calculateargmax(i, likelyhood_table, cpp, keys, attributes)
        if argmax == i[6]:
            correct +=1
        else:
            incorrect +=1
    percent_correct = correct / float(correct+incorrect) *100
    print percent_correct


test_data(test, l, cpp, keys, attributes)



trainingSet, testSet = splitDataset(dataset, splitRatio)
print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
# prepare model
# summaries = summarizeByClass(trainingSet)
# test model
# predictions = getPredictions(summaries, testSet)
# accuracy = getAccuracy(testSet, predictions)
# print('Accuracy: {0}%').format(accuracy)

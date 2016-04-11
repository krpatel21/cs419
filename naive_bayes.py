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
    for k in keys:
        tup = cpp[k]
        for i in f[k]:
            for j in f[k][i]:
                f[k][i] = j/float(tup[1])
    return f
pprint.pprint(likelyhood_table(f, keys, cpp))

def mean(numbers):
    return sum(numbers) / float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)


def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


trainingSet, testSet = splitDataset(dataset, splitRatio)
print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
# prepare model
# summaries = summarizeByClass(trainingSet)
# test model
# predictions = getPredictions(summaries, testSet)
# accuracy = getAccuracy(testSet, predictions)
# print('Accuracy: {0}%').format(accuracy)

# Kaushal Patel CS419 Spring 2016

import os, os.path
import sys

# determines if review is good
def isGood(text):
    words = text.split(" ")
    bad_words = 0
    good_words = 0
    for word in words:
        if word == ("good" or "excellent" or "great" or "amazing" or "liked" or "like" or "loved" or "enjoyed"):
            good_words = good_words + 1
        if word == ("bad" or "disappointing" or "predictable" or "plain" or "disappointment" or "disappoint" or
                        "horrible" or "sad" or "suck" or "hate" or "boring"):
            bad_words = bad_words + 1
    return good_words > bad_words

#main function. returns a tuple as specified in d2l
def predict(pos_data,neg_data):
    pos_files = directory(pos_data, ".txt")
    neg_files = directory(neg_data, ".txt")
    pos_count = 0
    neg_count = 0

    for f in os.listdir(pos_data):
        path = pos_data + "/" + f
        file = open(path)
        t =file.read()
        file.close
        if (isGood(t)):
            pos_count = pos_count + 1

    for f in os.listdir(neg_data):
        path = neg_data + "/" + f
        file = open(path)
        t =file.read()
        file.close
        if (not isGood(t)):
            neg_count = neg_count + 1

    pos_percentage = float(pos_count)/float(pos_files) * 100
    neg_percentage = float(neg_count)/float(neg_files) * 100

    tup = (pos_percentage, neg_percentage)
    return tup

# counts the number of txt files in the directory
def directory(path,extension):
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count

#gets the argument list
argList = sys.argv

# assume the first argument is the path for positive reviews
pd = argList[1]
nd = argList[2]

tup = predict(pd, nd)
print "Correctly classified" ,tup[0] ,"% of pos,",tup[1], "% neg"

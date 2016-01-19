# Kaushal Patel CS419 Spring 2016

import os, os.path
import sys

# figure out if review is positive
def isPos (text):
    words = text.split(" ")
    # return words
    for word in words:
        if word == ("good" or "excellent" or "great" or "amazing"):
            return True
    return False

# figure out if review is negative
def isNeg (text):
    words = text.split(" ")
    # return words
    for word in words:
        if word == ("bad" or "disappointing" or "disappointment" or "horrible" or "sad"):
            return True
    return False

def isGood(text):
    words = text.split(" ")
    bad_words = 0
    good_words = 0
    for word in words:
        if word == ("good" or "excellent" or "great" or "amazing"):
            good_words = good_words + 1
        if word == ("bad" or "disappointing" or "disappointment" or "horrible" or "sad"):
            bad_words = bad_words + 1
    return good_words > bad_words

#main function. returns a tuple as specified in the directions
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

    pos_avg = float(pos_count)/float(pos_files) * 100
    neg_avg = float(neg_count)/float(neg_files) * 100

    tup = (pos_avg, neg_avg)
    return tup

# counts the number of txt files in the directory
def directory(path,extension):
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count


argList = sys.argv

pd = argList[1]
nd = argList[2]

if __name__ == "__main__":
    tup = predict(pd, nd)
    print "Correctly classified" ,tup[0] ,"% of pos,",tup[1], "% neg"

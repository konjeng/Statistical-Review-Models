import csv
import scipy.io as sio
import numpy as np
import json

def parse(filename):
    pos_set = set([])
    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            pos_set.add(row[0].lower())

    pos_set = list(pos_set)
    return pos_set

# get the labels for training
def label_for_train():
    labels = []
    count = 0
    dict1 = {}
    with open('/home/gupta/Desktop/final_labels.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            review_id = int(row[1])
            rating = int(row[0])
            dict1[review_id] = rating;

    return dict1

# get the test reviews
def test_reviews(filename):
    pos_set = parse(filename)
    pos_test = []

    for j in pos_set:
        pos_list = [0]*len(pos_set)
        index = pos_set.index(j)
        pos_list[index] += 1
        pos_test.append(pos_list)

    return np.array(pos_test), pos_set
    # print np.array(pos_test), pos_set

def final_review(testVecs):
    data = sio.loadmat('nbOut_adv.mat')
    x = data['nbOut']
    results = {}
    for i in xrange(len(testVecs)):
        score =  round(1+(x[0][i]/5.),1)
        print score
        results[testVecs[i]] = score

    json.dump(results, open("nbResults_adv.txt", 'w'))

if __name__ == "__main__":
    # parse('adjectives.csv')
    # label_for_train()
    testArr, testVecs = test_reviews('data/concatenated_adjectives.csv')
    # final_review(testVecs)
    sio.savemat('testConcat.mat', {'testConcat':testArr})

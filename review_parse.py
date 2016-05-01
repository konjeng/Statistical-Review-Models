import csv
import numpy as np
import scipy.io as sio

def parse(filename):
    pos_set = set([])
    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            pos_set.add(row[0].lower())

    pos_set = list(pos_set)
    # print pos_set
    return pos_set

def review_parse(filename):
    pos_set = parse(filename)
    pos_list = []
    pos_train = []
    pos_train = [[0 for i in xrange(len(pos_set))] for x in xrange(26833)]

    with open(filename, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            sentence_id = int(row[0])-1
            word = row[1]
            final_word = word[1:len(word)-1].lower()
            pos = final_word
            index = pos_set.index(pos)
            pos_train[sentence_id][index] += 1

    final_review = []
    count = 0
    for i in pos_train:
        test = sum(i)
        if test != 0:
            newList = [float(x)/float(test) for x in i]
        # else:
            newList = i
        final_review.append(newList)
        count += 1

    final_review = np.array(final_review)
    print final_review.shape
    return final_review

if __name__ == "__main__":
    # pos_arr = review_parse('concatenated_adjectives.csv')
    # sio.savemat('concatenated_adjectives.mat', {'conData': pos_arr})

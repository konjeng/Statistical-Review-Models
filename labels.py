import csv
import scipy.io as sio
import numpy as np

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

def get_labels():
    labels = label_for_train()
    count = 0
    final_labels = [0 for i in xrange(26833)]
    with open('/home/gupta/Desktop/need_sentence.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            review_id = int(row[1])
            final_labels[count] = labels[review_id]
            count += 1

    sio.savemat('labels.mat', {'labelData': np.array(final_labels)})

get_labels()

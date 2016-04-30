import scipy
import scipy.io as sio
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import pickle

class NaiveBayes():
    def __init__(self):
        self.clf = GaussianNB()
        self.accuracy = 0
        self.y_out = []

    def train(self, X_train, y_train):
        self.clf.fit(X_train, y_train.ravel())

    def test(self, X_test):
        self.y_out = self.clf.predict(X_test)

    def score(self, X_test, y_test):
        self.accuracy = self.clf.score(X_test, y_test.ravel())

def test_reviews(filename):
    pos_set = BOW.parse(filename)
    count = 1
    pos_test = []

    for j in pos_set:
        pos_list = [0]*len(pos_set)
        index = pos_set.index(j)
        pos_list[index] += 1
        pos_test.append(pos_list)

    return np.array(pos_test), pos_set

def main():
    # get data
    data = sio.loadmat('adverbs.mat')
    X = data['advData']

    # get labels
    labels = sio.loadmat('labels.mat')
    y = labels['labelData']
    y = y.T

    # X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=42)
    X_train = X
    y_train = y

    # classifier module
    nbClassifier = NaiveBayes()
    # fit model
    nbClassifier.train(X_train, y_train)
    joblib.dump(nbClassifier.clf, 'nb_adv.pkl')
    # get accuracy
    nbClassifier.score(X_test, y_test)
    print nbClassifier.accuracy
    # clf = joblib.load("ADV Pickle Files/nb_adv.pkl")
    # testData = sio.loadmat('testAdv.mat')
    # X_train = testData['testAdv']
    # testOut = clf.predict(X_train)
    # sio.savemat('nbOut_adv.mat', {'nbOut':testOut})

if __name__=="__main__":
    main()

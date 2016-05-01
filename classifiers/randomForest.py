import scipy
import scipy.io as sio
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.externals import joblib
import pickle

class RandomForest():
    def __init__(self):
        self.rf = RandomForestClassifier(n_estimators=150, min_samples_split=2, n_jobs=-1)
        self.accuracy = 0
        self.y_out = []

    def train(self, X_train, y_train):
        self.rf.fit(X_train, y_train.ravel())

    def test(self, X_test):
        self.y_out = self.rf.predict(X_test)

    def score(self, X_test, y_test):
        self.accuracy = self.rf.score(X_test, y_test.ravel())

def main():
    # get data
    data = sio.loadmat('concatenated_adjectives.mat')
    X = data['conData']

    # get labels
    labels = sio.loadmat('labels.mat')
    y = labels['labelData']
    y = y.T
    #

    X_train = X
    y_train = y

    # forest
    rfClassifier = RandomForest()
    # fit model
    rfClassifier.train(X, y)
    joblib.dump(rfClassifier.rf, 'rf_concat.pkl')
    # get accuracy
    # clf = joblib.load("ADV Pickle Files/rf_adv.pkl")
    # testData = sio.loadmat('testAdv.mat')
    # X_train = testData['testAdv']
    # testOut = clf.predict(X_train)
    # sio.savemat('rfOut_adv.mat', {'rfOut':testOut})

if __name__=="__main__":
    main()

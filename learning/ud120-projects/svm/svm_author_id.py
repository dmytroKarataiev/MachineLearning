#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

# Import Support Vector Machine classifier
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
clf = SVC(kernel="linear")


def lessCode():
    ## Les code version
    clf.fit(features_train, labels_train)
    print clf.score(features_test, labels_test)


def timingVersion():
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time() - t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "predicting time:", round(time() - t0, 3), "s"

    # calculate number of letters from one sender
    total = [i for i in pred if i == 1]
    print len(total)

    t0 = time()
    accuracy = clf.score(features_test, labels_test)
    print "scoring time:", round(time() - t0, 3), "s"

    print accuracy


def lessAccuracy():
    global features_train
    features_train = features_train[:len(features_train) / 100]
    global labels_train
    labels_train = labels_train[:len(labels_train) / 100]
    timingVersion()


def rbf():
    global clf
    clf = SVC(kernel="rbf", C=10000.0)
    lessAccuracy()


def rbfFull():
    global clf
    clf = SVC(kernel="rbf", C=10000.0)
    timingVersion()


#########################################################

# rbfFull()
rbf()

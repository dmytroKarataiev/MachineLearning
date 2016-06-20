#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from learning.algorithms.class_vis import prettyPicture, output_image
from learning.algorithms.prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from sklearn.tree import DecisionTreeClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()

def classify(features_train, labels_train, leaf=2):
    ### your code goes here--should return a trained decision tree classifer
    clf = DecisionTreeClassifier(min_samples_leaf=leaf)
    clf.fit(features_train, labels_train)
    return clf


### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf2 = DecisionTreeClassifier(min_samples_split=2)
clf2.fit(features_train, labels_train)
print clf2.score(features_test, labels_test)

clf50 = DecisionTreeClassifier(min_samples_split=50)
clf50.fit(features_train, labels_train)
print clf50.score(features_test, labels_test)

#### grader code, do not modify below this line
# prettyPicture(clf, features_test, labels_test)
# output_image("test.png", "png", open("test.png", "rb").read())

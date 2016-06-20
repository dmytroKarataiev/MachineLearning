#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]


#### initial visualization
def visualise():
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
    plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.show()


################################################################################

### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
def kNeighbors(features_train, labels_train, features_test, labels_test):
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(features_train, labels_train)
    print "K-Neighbors accuracy: ", clf.score(features_test, labels_test)
    makePicture(clf, "kneighbors")


def randomForests(features_train, labels_train, features_test, labels_test):
    clf = RandomForestClassifier()
    clf.fit(features_train, labels_train)
    print "Random Forests accuracy: ", clf.score(features_test, labels_test)
    makePicture(clf, "rforests")


def adaBoost(features_train, labels_train, features_test, labels_test):
    clf = AdaBoostClassifier()
    clf.fit(features_train, labels_train)
    print "Ada Boost accuracy: ", clf.score(features_test, labels_test)
    makePicture(clf, "adaboost")


def makePicture(clf, name):
    try:
        prettyPicture(clf, features_test, labels_test, name)
    except NameError:
        pass


kNeighbors(features_train, labels_train, features_test, labels_test)
randomForests(features_train, labels_train, features_test, labels_test)
adaBoost(features_train, labels_train, features_test, labels_test)

#-----------------------------------

#
#   In this exercise we write a perceptron class
#   which can update its weights
#
#   Your job is to finish the train method so that it implements the perceptron update rule

import numpy as np

class Perceptron:

    def activate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        '''

        #First calculate the strength with which the perceptron fires
        strength = np.dot(values,self.weights)

        if strength>self.threshold:
            result = 1
        else:
            result = 0
        print "result: ", result
        return result

    def compare(self, value, target):
        print value, target
        if value == target:
            return 0
        elif value > target:
            return -1
        elif value < target:
            return 1

    def update(self,values,train,eta=.1):
        '''Takes in a 2D array @param values consisting of a LIST of inputs
        and a 1D array @param train, consisting of a corresponding list of
        expected outputs.
        Updates internal weights according to the perceptron training rule
        using these values and an optional learning rate, @param eta.
        '''
        #YOUR CODE HERE
        #update self.weights based on the training data
        newWeights = self.weights
        for element in range(len(values)):
            print values[element], train[element]
            temp = np.multiply(values[element], self.compare(self.activate(values[element]), train[element]))
            subs = np.multiply(temp, eta)
            newWeights = np.add(newWeights, subs)
            print temp, subs, newWeights

        return newWeights

    def __init__(self,weights=None,threshold=None):
        if weights is not None:
            self.weights = weights
        if threshold is not None:
            self.threshold = threshold

perc = Perceptron([1, 2, 3], 0)

print perc.update([[3, 2, 1], [4, 1, 5]], [0, 0], 0.1)


# Given weights for the hidden layer of [1, 1, -5] and [3, -4, 2],
# and weights for the output layer of [2, -1], what will this network output for inputs [1, 2, 3]?
print np.dot([1, 2, 3], [1, 1, -5])
print np.dot([1, 2, 3], [3, -4, 2])
print np.dot([-12, 1], [2, -1])
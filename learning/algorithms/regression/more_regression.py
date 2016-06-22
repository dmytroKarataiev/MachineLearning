#
#
# Regression and Classification programming exercises
#
#


#
#	In this exercise we will be taking a small data set and computing a linear function
#	that fits it, by hand.
#

#	the data set

import numpy as np

sleep = [5, 6, 7, 8, 10]
scores = [65, 51, 75, 75, 86]


def compute_regression(sleep, scores):

    #	First, compute the average amount of each list
    avg_sleep = np.mean(sleep)
    avg_scores = np.mean(scores)
    print avg_sleep, avg_scores

    #	Then normalize the lists by subtracting the mean value from each entry
    normalized_sleep = np.array(sleep) - avg_sleep
    normalized_scores = np.array(scores) - avg_scores
    print normalized_sleep
    print normalized_scores

    #	Compute the slope of the line by taking the sum over each student
    #	of the product of their normalized sleep times their normalized test score.
    #	Then divide this by the sum of squares of the normalized sleep times.

    slope = np.sum(normalized_sleep * normalized_scores) / np.sum(np.square(normalized_sleep))
    print slope

    #	Finally, We have a linear function of the form
    #	y - avg_y = slope * ( x - avg_x )
    #	Rewrite this function in the form
    #	y = m * x + b
    #	Then return the values m, b

    return slope, avg_scores - (avg_sleep * slope)

#
#	Polynomial Regression
#
#	In this exercise we will examine more complex models of test grades as a function of
#	sleep using numpy.polyfit to determine a good relationship and incorporating more data.
#
#
#   at the end, store the coefficients of the polynomial you found in coeffs
#

def polyRegression():
    sleep = [5,6,7,8,10,12,16]
    scores = [65,51,75,75,86,80,0]
    coeffs = np.polyfit(sleep, scores, 2)
    return coeffs


if __name__ == "__main__":
    m, b = compute_regression(sleep, scores)
    print "Your linear model is y={}*x+{}".format(m, b)
    print "Polynomial regression: ", polyRegression()

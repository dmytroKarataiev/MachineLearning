""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):

    maximum = max(arr)
    minimum = min(arr)

    if maximum == minimum:
        return 0.5
    else:
        return [rescale(minimum, maximum, each) for each in arr]

def rescale(minimum, maximum, feature):
    return (feature - minimum) / float((maximum - minimum))

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)


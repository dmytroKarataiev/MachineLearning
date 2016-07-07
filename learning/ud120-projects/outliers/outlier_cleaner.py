#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    errors = []

    for each in range(len(predictions)):
        errors.append(abs(predictions[each] - net_worths[each]))

    for each in range(len(ages)):
        cleaned_data.append((ages[each], net_worths[each], errors[each]))

    cleaned_data = sorted(cleaned_data, key = lambda x: x[2])

    print cleaned_data[:10]

    ### your code goes here
#   print predictions

#    print ages

#    print net_worths
    print len(cleaned_data), (int(len(cleaned_data) - len(cleaned_data) * 0.1))
    
    return cleaned_data[:int(len(cleaned_data) - len(cleaned_data) * 0.1)]


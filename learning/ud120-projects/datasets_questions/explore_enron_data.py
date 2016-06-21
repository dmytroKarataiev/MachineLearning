#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle, math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Size of the dataset
print "Size of the dataset: ", len(enron_data)

# Number of features
for key in enron_data:
    print "Number of features: ", len(enron_data[key])
    break

# Number of POI
print "Number of POI: ", len([i for i in enron_data if enron_data[i]['poi'] == 1])

# Num of Stocks for James Prentice, Jeffrey Skilling
list = [name for name in enron_data.keys() if ("JAMES" in name and "PRENTICE" in name) or "SKILLING" in name]

for name in list:
    print "Values of stocks for: ", name, enron_data[name]["total_stock_value"]
    print "Excercised stock options: ", name, enron_data[name]["exercised_stock_options"]

# Num of letters from Wesley Colwell to POI
print "Num of letters from Wesley to POI: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# Largest sum of money from top seniors
list = [name for name in enron_data.keys() if "LAY" in name or "SKILLING" in name or "FASTOW" in name]

largest = []
for name in list:
    if len(largest) == 0:
        largest.append((name, enron_data[name]["total_payments"]))
    else:
        if largest[0][1] < enron_data[name]["total_payments"]:
            largest[0] = (name, enron_data[name]["total_payments"])
print "Man who made the most: ", largest

# Quantified salary
list = [name for name in enron_data.keys() if enron_data[name]["salary"] != "NaN"]
print "Have salaries: ", len(list)

list = [name for name in enron_data.keys() if enron_data[name]["email_address"] != "NaN"]
print "Have emails: ", len(list)

list = [name for name in enron_data.keys() if enron_data[name]["total_payments"] != "NaN"]
print "Percentage of people who don't have values for salaries: ", len(enron_data) - len(list), ((len(enron_data) - len(list)) / float (len(enron_data)))

list = [name for name in enron_data.keys() if enron_data[name]["total_payments"] == "NaN" and enron_data[name]["poi"]]
print "Number of POIs without payments: ", len(list)

list = [name for name in enron_data.keys() if enron_data[name]["poi"]]
print "Number of POIs: ", len(list)


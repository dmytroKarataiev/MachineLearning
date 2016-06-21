#!/usr/bin/python

# Calculates number of POI in the file
# As we now file formatting, we can count all lines with ( at the beginning

names = open("poi_names.txt")

poiNumber = 0
for line in names:
    if line.startswith("("):
        print line
        poiNumber += 1
print poiNumber

names.close()
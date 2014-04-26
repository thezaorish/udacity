#!/usr/bin/python

__author__ = 'training'

import sys

# Loop around the data
# It will be in the format key\tval
# Where key is the item description, val is the sale amount
#
# All the sales for a particular store will be presented, then the key will change and we'll be dealing with the next store

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal

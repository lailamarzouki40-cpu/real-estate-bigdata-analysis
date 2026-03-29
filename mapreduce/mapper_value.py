#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
for row in reader:
    if not row or row[0] == 'address':
        continue
    try:
        zipcode = row[4]
        price = float(row[1])
        sqft = float(row[3])
        print("{0}\t{1},{2}".format(zipcode, price, sqft))
    except (IndexError, ValueError):
        continue
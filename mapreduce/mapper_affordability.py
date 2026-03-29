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
        beds = float(row[2])
        # Use .format() instead of f-strings
        print("{0}\t{1},{2}".format(zipcode, price, beds))
    except (IndexError, ValueError):
        continue
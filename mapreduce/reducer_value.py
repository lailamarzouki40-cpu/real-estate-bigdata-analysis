#!/usr/bin/env python3
import sys

current_zip = None
sum_price = 0
sum_sqft = 0

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    
    zipcode, data = line.split('\t')
    price, sqft = map(float, data.split(','))
    
    if current_zip == zipcode:
        sum_price += price
        sum_sqft += sqft
    else:
        if current_zip:
            price_per_sqft = sum_price / sum_sqft if sum_sqft > 0 else 0
            print("{0}\t{1:.2f}".format(current_zip, price_per_sqft))
        current_zip = zipcode
        sum_price = price
        sum_sqft = sqft

if current_zip:
    price_per_sqft = sum_price / sum_sqft if sum_sqft > 0 else 0
    print("{0}\t{1:.2f}".format(current_zip, price_per_sqft))
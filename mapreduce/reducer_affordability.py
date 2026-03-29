#!/usr/bin/env python3
import sys

current_zip = None
sum_price = 0
sum_beds = 0

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    
    zipcode, data = line.split('\t')
    price, beds = map(float, data.split(','))
    
    if current_zip == zipcode:
        sum_price += price
        sum_beds += beds
    else:
        if current_zip:
            avg_per_bed = sum_price / sum_beds if sum_beds > 0 else 0
            print("{0}\t{1:.2f}".format(current_zip, avg_per_bed))
        current_zip = zipcode
        sum_price = price
        sum_beds = beds

if current_zip:
    avg_per_bed = sum_price / sum_beds if sum_beds > 0 else 0
    print("{0}\t{1:.2f}".format(current_zip, avg_per_bed))
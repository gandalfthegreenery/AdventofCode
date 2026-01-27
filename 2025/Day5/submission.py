import io
import numpy as np


f= open("AdventofCodeDay5.txt","r") 
ranges = []
ids_fresh = 0
for row in f:
    if len(row.split("-"))==2:
        ranges.append((int(row.split("-")[0]),int(row.split("-")[1])))
sorted_ranges = sorted(ranges)
ids_fresh = 0
prev_low = sorted_ranges[0][0]
prev_high = sorted_ranges[0][1]
counted = False

for low,high in sorted_ranges:
    if low <=prev_high:
        prev_high = max(high,prev_high)
    else:
        ids_fresh+=prev_high-prev_low+1
        prev_low = low
        prev_high = high

ids_fresh+=prev_high-prev_low+1

print("fresh",ids_fresh)
f.close()
        

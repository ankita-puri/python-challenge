import os
import csv
from typing import Counter
csvpath = os.path.join('..', 'Resources', 'PyBank.csv')
# with open(csvpath) as fin:
#     headerline = fin.next()
#     total = 0
#     for row in csv.reader(fin):
#         total += int(row[1])
#     print (total)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    total = 0
    for row in csvreader:
        total += int(row[1])
    print (total)
    print(f"CSV Header: {csv_header}")
    
    # row_count = sum(1 for row in csvfile)
    # print(row_count )

# total = 0
# for row in csvreader:  
#    total += int(row[1])
#    print(total)

import csv
import os

l = []
with open('nouns.csv', 'r') as csvfile:
    readerrow = csv.reader(csvfile, delimiter = ',', quotechar='|')
    for row in readerrow:
        l.append(row[1])

final_set = set(l)
print final_set

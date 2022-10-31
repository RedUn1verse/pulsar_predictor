import csv
import random

file = open("raw_pulsar_data.csv")
csv_reader = csv.reader(file)
print (type(file))

rows = []
for row in csv_reader:
        rows.append(row)
print (rows)
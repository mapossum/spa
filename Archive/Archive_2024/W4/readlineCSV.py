import csv

f = open("Presidents.csv", "r")

csvFile = csv.reader(f)

presList = []
for line in csvFile:
    presList.append(line)

print(presList)

f.close()

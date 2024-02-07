import csv

import statistics

f = open("points2.txt", "r")

csvFile = csv.reader(f,delimiter=' ')

xlist = []
ylist = []
for line in csvFile:
    x, y = line
    x,y = ([int(x),int(y)])
    xlist.append(x)
    ylist.append(y)
    
    

print(statistics.mean(xlist))

import math
import haversine

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

#dist = distance(0,0,3,4)
#print(dist)

#open a file
f = open("points.txt", "r")

#setup lastx and lasty vars to equal something 

for line in f:
    ls = line.split()
    x = float(ls[0])
    y = float(ls[1])

    #Code that calculates the distance between the current point and the last point 
    segmentDistance = distance(lastx, lasty ,x,y)

    #Accumulate each segmentDistance into overall distance

    lastx = x
    lasty = y

    
    print(segmentDistance)

f.close()

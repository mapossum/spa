import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

#This demos how to use distance
#mydistance = distance(0,0,3,4)
#print(mydistance)

#open a file
f = open("points.txt", "r")

previousx = -1
previousy = -1
totaldistance = 0

for line in f:
    ls = line.split()
    x = float(ls[0])
    y = float(ls[1])
    print(x,y)

    if previousx != -1:
        #find distance to previous point
        mydistance = distance(previousx,previousy,x,y)
        #Add to total distance
        totaldistance = mydistance + totaldistance
        

    previousx = x
    previousy = y

#Report total distance

f.close()

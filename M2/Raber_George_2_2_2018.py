import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

firsttime = True
totaldistance = 0
keepgoing = True

while(keepgoing):

    #Have the user give us a point as two numebers (X and Y)

    x = float(raw_input("X value for point along line:"))
    y = float(raw_input("Y value for point along line:"))

    #Test if there is a previous x and y and if not assign one
    if firsttime:
        prex = x
        prey = y
    
    firsttime = False
    
    #Figure out the distance from current point to the previous point

    cdist = distance(prex,prey,x,y)
    print cdist, prex, prey, x, y
    
    #Add that distance to the running total

    totaldistance = cdist + totaldistance

    #Find out if they want to continue

    cont = raw_input("Do you want to continue? (Enter Y to keep going)")

    #If they want to continue ask for another point

    if (cont == "Y"):
        prex = x
        prey = y
    else:
        #If not report the total distance
        print totaldistance
        keepgoing = False
    

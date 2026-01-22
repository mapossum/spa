

def findDistance(x1,y1,x2,y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

n = 0
totalDistance = 0

#start here with intial point
lx = float(input("Enter intial x coordinate: "))
ly = float(input("Enter inital y coordinate: "))

while(True):
    #Get a point from the user
    
    x = float(input("Enter next x coordinate: "))
    y = float(input("Enter next y coordinate: "))

    #Find the distance from the current point the last point
    #call findDistance
    distance = findDistance(lx,ly,x,y)

    #add up running total
    totalDistance = totalDistance + distance
    
    #Find out if the user wants to keep going.

    #if not stop if so just keep going in loop
    
    n = n + 1

    print(totalDistance)

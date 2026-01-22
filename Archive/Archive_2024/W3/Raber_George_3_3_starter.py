from haversine import points2distance

n = 0
totalDistance = 0

#start here with intial point
lx = float(input("Enter intial long coordinate: "))
ly = float(input("Enter inital lat coordinate: "))

while(True):
    #Get a point from the user
    
    x = float(input("Enter next lon coordinate: "))
    y = float(input("Enter next lat coordinate: "))

    #Find the distance from the current point the last point
    #call findDistance
    distance = points2distance(lx,ly,x,y)

    #add up running total
    totalDistance = totalDistance + distance
    
    #Find out if the user wants to keep going.

    #if not stop if so just keep going in loop
    
    n = n + 1

    print(totalDistance)

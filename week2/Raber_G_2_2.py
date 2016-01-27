import math

def distance(x1,y1,x2,y2):

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


#print distance(3,8,6,12)

#Gather inital values
total = 0
px = raw_input("Enter x: ")
py = raw_input("Enter y: ")
px = float(px)
py = float(py)
    
while (True):
    #user input
    cx = raw_input("Enter x: ")
    cy = raw_input("Enter y: ")
    cx = float(cx)
    cy = float(cy)
    currentdist = distance(px,py,cx,cy)
    total += currentdist
    print currentdist, total
    px = cx
    py = cy
    #Prompt User to Continue
    #use and if then statement to special pharse to stop

#While Loop
    #get new point
    #calc distance
    #find new total distance

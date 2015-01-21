import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

x1 = raw_input("Enter x coord: ")
y1 = raw_input("Enter y coord: ")
x1 = float(x1)
y1 = float(y1)

totaldistance = 0
answer = "yes"
while(answer == "yes"):

    x2 = raw_input("Enter x coord: ")
    y2 = raw_input("Enter y coord: ")
    x2 = float(x2)
    y2 = float(y2)

    #Calculate distance
    #print distance(x1,y1,x2,y2)
    totaldistance = ??????
    print totaldistance

    #ask the user to go again?
    answer = raw_input("do you have more points? ")

    x1 = x2
    y1 = y2

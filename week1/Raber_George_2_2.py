import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

#print distance(3,0.5,0,4)
done = ""
prexval = None

totaldistance = 0

while (done == ""):
    xval = raw_input("Enter X Value: ")
    yval = raw_input("Enter Y Value: ")
    done = raw_input("Enter Y if done, press Enter if not done: ")
    xval = float(xval)
    yval = float(yval)
    if not (prexval == None):
        totaldistance = totaldistance + distance(prexval,preyval,xval,yval)

    prexval = xval
    preyval = yval

print totaldistance


def isTriangle(a,b,c):
    
    if ((a + b) >= c):
        if((a + c) >= b):
            if ((b+c) >= a):
                return True
    return False

def isTriangle2(a,b,c):

    if (((a + b) >= c) and ((a + c) >= b) and ((b+c) >= a)):
        return True
    else:
        return False

x = raw_input("Enter first side: ")
y = raw_input("Enter second side: ")
z = raw_input("Enter third side: ")


if (isTriangle(float(x),float(y),float(z))):
    print "Yes"
else:
    print "No"

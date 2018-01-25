
#This function tests two numbers and returns the largest number
def whichisbigger(x,y):
    if (x > y):
        return x
    elif (x == y):
        return x
        #This is an example of dead code that will never run
        #It won't run because the return statement is above it.
        print "they are the same"
    else:
        return y

stop = False

while (stop == False):
    x = raw_input("Provide a number:")
    y = raw_input("Provide another number:")

    try:
        x = float(x)
        y = float(y)
    except:
        print "Those arn't numbers, defaulting to alpha order"

    # These are a few tests of the function
    print "The biggest number is: " + str(whichisbigger(x,y))

    wannaStop = raw_input("Do you want to stop testing? (enter Y to stop):")

    if (wannaStop == "Y"):
        stop = True
    else:
        pass
    

print "Done"

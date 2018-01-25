x = 40
y = 20

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


# These are a few tests of the function
print whichisbigger(x,y)
print whichisbigger(30,12)
print whichisbigger(18,20)






print "Done"

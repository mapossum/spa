x = 40
y = 20

def whichisbigger(x,y):
    if (x > y):
        print "x is bigger"
        return x
    elif (x == y):
        print "they are equal"
        print "Isn't that awesome"
        if (x == 7):
            print "And they are both sevens!"
        return x
    else:
        print "y is bigger"
        return y



bigger = whichisbigger(x,y)

print x
print bigger





print "Done"

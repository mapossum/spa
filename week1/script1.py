
import math

def findhy(a,b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c

def iseven(i):
    x = i % 2
    if (x == 0):
        return True
    else:
        return False

def isevenshort(i):
    return not(i % 2)

def ism(i,n):
    return not(i % n)
    
    
leg1 = 2.2
leg2 = 7

hy = findhy(leg1, leg2)

print hy

print iseven(7)

print isevenshort(7)

print ism(4,2)

print ism(5,4)







##if (hy > 5):
##    print "That is bigger than 5"
##    print "yes it is"
##    if (leg1 > 1):
##        print "and leg 1 is bigger than 1"
##
##else:
##    print "That is smaller than 5"
##





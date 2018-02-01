

def is_triangle(a,b,c):
    t1, t2, t3 = False, False, False
    if (a + b) > c:
        t1 = True
    if (b + c) > a:
        t2 = True
    if (c + a) > b:
        t3 = True
    if (t1 and t2 and t3):
        print "Yes"
    else:
        print "No"
    return t1 and t2 and t3

output = is_triangle(2,2,5)
print output

#add code to get three stick lengths from user and then call in_triangle with those values

#Report to the user if it can be a triangle in a complete sentance.
        

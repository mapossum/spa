
def is_triangle(a,b,c):
    
    if (a > b + c) or (b > c + a) or (c > a + b):
        print "Not a Trianlge"
    else:
        print "Is a Triangle"


s = raw_input('Enter First Leg: ')
s = int(s)

s = raw_input('Enter First Leg: ')
s = int(s)

s = raw_input('Enter First Leg: ')
s = int(s)



is_triangle(s,4,5)

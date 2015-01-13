

#Demo of Recursive
def minus0(a):
    print a
    a = a - 1
    if not (a == 0):
        minus0(a)
    else:
        print "Blastoff"

#Demo of While
def minus1(a):
    while (a > 0):
        print a
        a = a - 1
    print "Blastoff"

#Demo of For
def minus2(a):
    for n in range(0,a):
        print (a - n)
    print "Blastoff"
    
    

minus0(5)
minus1(5)
minus2(5)



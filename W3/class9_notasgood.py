#doing the same thing but not as well

doit = True

while doit:
    a = input("Provide a number: ")
    try:
        #attempt to run this code
        a = float(a)
    except:
        #if that code above fails run this code
        print("'", a, "' cannot be converted into a number")
        doit = True
    else:
        doit = False

b = 10.0

if (a > b):
    print("a is bigger")
elif (a == b):
    print("a and b are the same number")
else:
    print("b is bigger")

    
    

#fruitful functions and recursion comparison operations

def getaNumber():
    ina = input("Provide a number: ")
    try:
        #attempt to run this code
        ina = float(ina)
    except:
        #if that code above fails run this code
        print("'", ina, "' cannot be converted into a number")
        #what should it do?
        return getaNumber()
    else:
        return ina

a = getaNumber()
b = 10.0

if (a > b):
    print("a is bigger")
elif (a == b):
    print("a and b are the same number")
else:
    print("b is bigger")

    
    
#multiple comparison operations

a = input("Provide a number: ")
b = 10

try:
    #attempt to run this code
    a = int(a)
except:
    #if that code above fails run this code
    print("'", a, "' cannot be converted into a number")
else:
    if (a > b):
        print("a is bigger")
    elif (a == b):
        print("a and b are the same number")
    else:
        print("b is bigger")
finally:
    print("All Done")
    
    

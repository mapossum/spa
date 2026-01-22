
def blastoff(a):
    while(a):
        print(a)
        a = int(a - 1)    

    print("Bastoff!!")

a = input("Provide a number: ")

try:
    #attempt to run this code
    a = float(a)
except:
    #if that code above fails run this code
    print("'", a, "' cannot be converted into a number")
else:
    blastoff(a)

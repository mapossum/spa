
errorState = False

try:
    x1 = float(input("Provide the first X value: "))
    y1 = float(input("Provide the first Y value: "))
except:
    print("The value entered could not be converted into a number.")
    errorState = True
    
#We only want to excecute the code below if they have entered valid numbers

if errorState == False:    
    print(x1)
    print(type(x1))

    print(x1 + y1)

print("Have a nice day!")

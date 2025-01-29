

n = 11

#setup variable for running product before loop.
runningProduct = 1

#compute the factorial

ognumber = n
while (n > 0):
    runningProduct = runningProduct * n
    #This print statement helps us to debug and see what our code is doing as it executes
    #print(runningProduct, n)
    n = n - 1

report = "The factorial of {0} is {1}".format(ognumber, runningProduct)
print(report)

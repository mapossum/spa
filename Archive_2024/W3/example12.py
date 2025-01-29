
def factorial(n,s=1):

    #setup variable for running product before loop.
    runningProduct = 1

    #compute the factorial
    
    while (n > (s-1)):
        runningProduct = runningProduct * n
        n = n - 1
    
    return runningProduct

n = 11

factorialvalue = factorial(n)

report = "The factorial of {0} is {1}".format(n, factorialvalue)
print(report)


y = 20
z = 18

productRange = factorial(y,z)

report = "The product of all the number between {0} and {1} is {2}".format(y, z, productRange)
print(report)

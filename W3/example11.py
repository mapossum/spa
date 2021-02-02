
def factorial(n,s):

    #setup variable for running product before loop.
    runningProduct = 1

    #compute the factorial
    
    while (n > (s-1)):
        runningProduct = runningProduct * n
        n = n - 1
    
    return runningProduct

n = 11
x = 7

factorialvalue = factorial(n,x)

report = "The product of all the numbers from {0} to {1} is {2}".format(n, x, factorialvalue)
print(report)

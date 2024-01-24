
def factorial(n):

    #setup variable for running product before loop.
    runningProduct = 1

    #compute the factorial
    
    while (n > 0):
        runningProduct = runningProduct * n
        n = n - 1
    
    return runningProduct

n = 11

factorialvalue = factorial(n)

report = "The factorial of {0} is {1}".format(n, factorialvalue)
print(report)

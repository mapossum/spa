
def countdown(n=5):

    #countdown code
    if n < 1:
        print("Please use a positive number")
        return 0

    runningProduct = 1

    while (n > 0):
        print(n)
        runningProduct = runningProduct * n
        n = n - 1

    print("Blastoff!")

    return runningProduct

a = countdown(0)
print(a)

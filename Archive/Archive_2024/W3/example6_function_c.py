
def countdown(n=5):

    #countdown code

    runningProduct = 1

    while (n > 0):
        print(n)
        runningProduct = runningProduct * n
        n = n - 1

    print("Blastoff!")

    return runningProduct

n = 10
while n > 0:
    a = countdown(n)
    print(a)
    n = n - 1

def countLarge(inputList, largeNumber):

    total = 0
    for value in inputList:
        if (value > largeNumber):
            total = total + 1

    return total

#finds the average value of a list (or tuple)
def findStats(*t):
    LargeNumbers = -1
    if (len(t) > 1):
        #find the number of values greater than X
        x = t[1]
        LargeNumbers = countLarge(t[0],x)

    inputList = t[0]
    total = 0
    for value in inputList:
        total = total + value

    mean = float(total) / float(len(inputList))

    stDev = 0

    #Write Code to Calculate St.DEV
    #???
    # x = sum of (each value - mean) **2
    ## squareRoot(x / (len(inputList) - 1))

    #Modify total to be X above
    total = 0
    for value in inputList:
        total = total + value
    #######################

    if (LargeNumbers > -1):
        return total, mean, , stDev, LargeNumbers
    else:
        return total, mean, stDev

testList = [54,77.5,884,33]
print findStats(testList, 5)



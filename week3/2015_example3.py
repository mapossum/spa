#finds the average value of a list (or tuple)
def findMean(inputList):

    total = 0
    for value in inputList:
        total = total + value

    return float(total) / float(len(inputList))

#This function calculates total number of large number as defined by user
def countLarge(inputList, largeNumber):

    total = 0
    for value in inputList:
        if (value > largeNumber):
            total = total + 1

    return total

def squareListinPlace(inputList):
    count = 0
    for value in inputList:
        inputList[count] = value ** 2
        count = count + 1
    #return inputList

def squareList(inputList):

    outputlist = []
    for value in inputList:
        outputlist.append(value **2)

    return outputlist

#Filter function that returns a list of values over user input
def returnLarge(inputList, largeNumber):

    outputlist = []
    for value in inputList:
        if (value > largeNumber):
            outputlist.append(value)

    return outputlist


myList = [23,4,32,56,5463,456]

print findMean(myList)
print countLarge(myList, 100)

print squareList(myList)

#squareListinPlace(myList)
print myList

print returnLarge(myList,100)


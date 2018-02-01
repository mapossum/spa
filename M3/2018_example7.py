myList = []  # This creates and empty list

Cities = ["Hattiesburg, MS", "Irvine, CA", "Columbia, SC", "Calgary, AB"]

ages = [23,25,45,11,34, 56]

#my Map function to add a number to everyitem in a list

def addnList(myList, n):
    i = 0
    for number in myList:
        myList[i] = number + n
        i = i + 1

addnList(ages,3)

# Values of ages were modified in function
print ages


# my reduce function summarizes items in a list (caculate the mean)

def findMean(myList):
    tot = 0
    for number in myList:
        tot += number # tot = tot + number
    mean = float(tot) / len(myList)
    return mean

print findMean(ages)

# filter takes a list and only returns that values that meat a certain critera


def numsgreaterThan(myList, n):
    newList = []
    for number in myList:
        if number > n:
            newList.append(number)
    return newList

print numsgreaterThan(ages, 30)




    




    



myList = []  # This creates and empty list

Cities = ["Hattiesburg, MS", "Irvine, CA", "Columbia, SC", "Calgary, AB"]

ages = [23,25,45,11,34, 56]

#my Map function to add a number to everyitem in a list

def addnList(myList, n):
    newList = []
    for number in myList:
        newList.append(number + n)
    return newList

newages = addnList(ages,3)

print newages

    



import math

ages = [23,25,45,11,34,56]
ages2 = [23,25,25,23,26,56]

def stats(myList):
    #Find out if all values are number if not return None
    for val in myList:
        if not(type(val) == int or type(val) == float):
            return None

    #Calculate the stats and return        
    tot = 0
    for number in myList:
        tot += number # tot = tot + number
    mean = float(tot) / len(myList)

    #Calculate st dev

    #find all the deviations, square them, add them together and then div by n
    sqtot = 0
    for number in myList:
        sqtot += (number - mean) ** 2
    stdev = math.sqrt(float(sqtot) / (len(myList)-1))
    
    return tot, mean, stdev

print stats(ages)[0]



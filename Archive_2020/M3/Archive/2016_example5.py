import math

def getstats(mylist):
    total = 0

    for el in mylist:
        #print age
        total += el

    mean = float(total) / len(mylist)

    diftotal = 0
    #Calculate Standard Dev
    for el in mylist:
        diff = el - mean
        sqdiff = diff * diff
        diftotal += sqdiff

    variance = diftotal / len(mylist)
    stdev = math.sqrt(variance)

    return mean, stdev

ages = [34,45,23,46,21,18,33]

print ages

stats = getstats(ages)
print stats

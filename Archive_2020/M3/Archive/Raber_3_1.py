

def getStats(inList,num):
    total = 0
    for val in inList:
        if not(type(val) == type(1) or type(val) == type(1.0)):
            return 
        total += val
    return total, float(total) / len(inList)


mylist = [23,46,75,55,77]
print getStats(mylist,40)

import math

def simplefilter(mylist, x):
    filtered = []
    for n in mylist:
        if n > x:
            filtered.append(n)
    return filtered
    

temps = [34,45,23,46,21,18,33]


newvals = simplefilter(temps, 25)

print newvals


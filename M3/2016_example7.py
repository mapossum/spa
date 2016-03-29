import math

def ctok(mylist):
    kels = []
    for n in mylist:
        kels.append(n + 273)
    return kels

def ctof(mylist):
    fars = []
    for n in mylist:
        fars.append(n * 9/5.0 + 32.0)
    return fars

temps = [34,45,23,46,21,18,33]


newtemps = ctof(temps)
print newtemps
newtemps = ctok(temps)
print newtemps


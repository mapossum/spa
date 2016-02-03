import math

def ctok(mylist):
    c = 0
    for n in mylist:
        mylist[c] = n + 273
        c += 1

def ctof(mylist):
    c = 0
    for n in mylist:
        mylist[c] = n * 9/5.0 + 32.0
        c += 1

temps = [34,45,23,46,21,18,33]


ctof(temps)
print temps
ctok(temps)
print temps


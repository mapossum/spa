myd = { "George": 39, "April": 37, "Lloyd": 35 }

#Small cities Dictionary
Cites = {"Hattiesburg": {"Population" : 50000, "Area": 300}}

k = myd.keys()

k.sort()

print k

for x in k:
    print x, myd[x]


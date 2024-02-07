import csv

f = open("Presidents.csv", "r")

csvFile = csv.DictReader(f)

presList = []
for line in csvFile:
    presList.append(line)

print(presList)

f.close()


pss = {}

for p in presList:
    cstate = p["State"]
    if cstate in pss:
        pss[cstate] = pss[cstate] + 1
    else:
        pss[cstate] = 1

#This is code we googled
sortedpss = sorted(pss.items(), key=lambda x:x[1])


print(sortedpss)

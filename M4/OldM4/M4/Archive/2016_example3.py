bldgs = {"Kelly": 1, "Walker": 2, "Johnson": 12, "Lucas": 2}

f = open(r'C:\courses\spa\week4\outputTest.csv', 'w')

f.write("Building, Stories\n")

for bldg in bldgs:
    #f.write(bldg + "," + str(bldgs[bldg]) + "\n")
    f.write("%s,%s\n" % (bldg, bldgs[bldg]))

    
f.close()


#myd["Kelly"]

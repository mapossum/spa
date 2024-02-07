
f = open("Presidents.csv", "r")

presData = []
header = f.readline().strip().split(",")
for line in f:
    sline = line.strip()
    presData.append(sline.split(","))

    #use header to build dictionary each time through loop
    

f.close()

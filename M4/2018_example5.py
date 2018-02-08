import random

fread = open(r"C:\temp\spa\M4\citiesSmall.txt", "r")
fwrite = open(r"C:\temp\spa\M4\citiesSmallPipes.txt", "w")

for line in fread.readlines():
    lineData = line.strip().split(",")
    if len(lineData) < 2:
        #assume it is a header
        pass
    else:
        lineData.append(str(random.normalvariate(65,10)))
    fwrite.write("|".join(lineData) + "\n")

fread.close()
fwrite.close()







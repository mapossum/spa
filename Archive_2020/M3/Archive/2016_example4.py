import math
ages = [34,45,23,46,21,18,33]

print ages

total = 0

for age in ages:
    #print age
    total += age

mean = float(total) / len(ages)

diftotal = 0
#Calculate Standard Dev
for age in ages:
    diff = age - mean
    sqdiff = diff * diff
    diftotal += sqdiff

variance = diftotal / len(ages)
stdev = math.sqrt(variance)
print mean, stdev

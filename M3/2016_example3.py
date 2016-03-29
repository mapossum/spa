
ages = [34,45,23,46,21,18,33]

total = 0

for age in ages:
    print age
    total += age

print "The average age is:", float(total) / len(ages)

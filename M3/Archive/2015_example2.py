cities = ["Hattiesburg, MS", "New York, NY", 'Seattle, WA', 6]

print cities

myname = "Georgr"

#myname[5] = "e" don't work

myname = myname[:5] + "e"

#print myname

cities[-1] = "Irvine, CA"
print cities

# print cities.pop() removes last item and return

cities.append("Dallas, TX")

citiesunsort = cities[:]  #this is the code that you would do to make a copy of a list
cities.sort()
print cities
#print citiesunsort

print (" " * 5).join(cities)


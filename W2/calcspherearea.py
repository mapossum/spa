import math

from math import *

print(sin(10))

def calculate_and_print_sphere_volume(radius):
    b = 4/3
    e = radius**3
    volume = b * math.pi * e
    #volume = (4/3) * math.pi * radius**3
    print("The volume of the sphere with radius", radius, "is:", volume)

# Assign a number to the variable 'r'
r = 6.2

#r = str(r) #convert r to a string

# Call the function to calculate and print the volume
calculate_and_print_sphere_volume(r)
calculate_and_print_sphere_volume(3.1)

#print(type(r))
#print(type(calculate_and_print_sphere_volume))

def power(num,exp):
    print(num, "to the", exp, "is:", num**exp)
    print(str(num) + " to the " + str(exp) + " is: " + str(num**exp))

def powerF(num,exp):
    return num**exp 

power(2,3)

answer = powerF(2,3)
print(answer)

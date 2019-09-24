import arcpy

print "Hello"

#name = raw_input("What is your name? ")


print "Well Hello " + arcpy.GetParameterAsText(0)

print arcpy.GetArgumentCount()

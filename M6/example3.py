import arcpy

print "Hello"

print arcpy.GetArgumentCount()

nparms = arcpy.GetArgumentCount()

for x in range(0,nparms):
    print arcpy.GetParameterAsText(x)

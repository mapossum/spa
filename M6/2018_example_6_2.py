

import arcpy

print arcpy.GetArgumentCount()
a = arcpy.GetParameterAsText(0)
b = arcpy.GetParameterAsText(1)

# This is so that it runs outside of ArcGIS for testing.
if (a == ""):
    a = 5.0

if (b == ""):
    b = 10.0    

c = float(a) + float(b)
print c
arcpy.AddMessage("The sum of {1} and {2} is {0}".format(c, a, b)) #eqiv to "The sum is " + str(c)

arcpy.SetParameterAsText(2, c)

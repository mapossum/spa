

import arcpy

#These are for testing comment out the paramater lines below for testing
a = 3
b = 7

#Set up Input Paramaters
a = int(arcpy.GetParameterAsText(0))
b = float(arcpy.GetParameterAsText(1))

#Write and code and logic here
c = a + b

#Return values out to user
print(c)
arcpy.AddMessage("{0} plus {1} is {2}.".format(a,b,c))
#arcpy.AddMessage(str(a) + " plus " + str(b) + " is " + str(c) +".")
#If you add an error it will fail and return the string as red text to GP window.
#arcpy.AddError("Sorry it Failed")
if (b == 0):
    arcpy.AddWarning("Anything plus 0 is the same number")
arcpy.SetParameterAsText(2,c)

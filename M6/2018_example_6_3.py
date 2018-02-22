

import arcpy

def arcpyPrint(printstr):
    arcpy.AddMessage(printstr)
    print printstr
    
input1 = arcpy.GetParameterAsText(0) #first FC dataset
input2 = arcpy.GetParameterAsText(1) #second FC dataset
input3 = arcpy.GetParameterAsText(2) #Dissolve Field
output = arcpy.GetParameterAsText(3) #output FC location

# This is so that it runs outside of ArcGIS for testing.
if (input1 == ""):
    input1 = r"C:\temp\LabData.gdb\ctracts"

if (input2 == ""):
    input2 = r"C:\temp\LabData.gdb\watersheds"    

if (input3 == ""):
    input3 = "HUC_8"

if (output == ""):
    output = r"C:\temp\LabData.gdb\output"

arcpyPrint("Interseting " + input1 + " " + input2)
arcpy.Intersect_analysis([input1, input2], r"in_memory/tempint", "ALL")

arcpyPrint("Dissolving layers based on " + input3)
arcpy.Dissolve_management(r"in_memory/tempint", output,[input3])

#

import arcpy

nparms = arcpy.GetArgumentCount()

arcpy.AddMessage("You have specifed " + str(nparms) + " parameters")
arcpy.AddMessage(arcpy.GetParameterAsText(0))

#inputs
inputFeats = arcpy.GetParameterAsText(0)
bufd = arcpy.GetParameterAsText(1)

#outputs
outFeats = arcpy.GetParameterAsText(2) #r"C:\temp\growthM\tempOut.shp"

#Code to do our Process Here:
arcpy.Buffer_analysis(inputFeats, outFeats, bufd)
#arcpy.SetParameterAsText(2, outFeats)

arcpy.AddMessage("Completed")

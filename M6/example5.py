import arcpy


nparms = arcpy.GetArgumentCount()

arcpy.AddMessage("You have specifed " + str(nparms) + " parameters")
arcpy.AddMessage(arcpy.GetParameterAsText(0))

parms = arcpy.GetParameterAsText(0).split(";")

arcpy.AddMessage(parms)

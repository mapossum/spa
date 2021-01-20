import arcpy

arcpy.env.overwriteOutput = True

inFeatures = arcpy.GetParameterAsText(0)
popField = arcpy.GetParameterAsText(1)
inOverlay = arcpy.GetParameterAsText(2)
dissolveOutput = arcpy.GetParameterAsText(3)
intersectOutput = "in_memory/CWInterset"

arcpy.AddMessage( "Adding Field" )
arcpy.AddField_management(inFeatures, "Area", "DOUBLE")
arcpy.CalculateField_management(inFeatures, "Area", "!shape.area!", "PYTHON_9.3")

inFeatures = [inFeatures, inOverlay]
arcpy.AddMessage( "Intersecting" )
arcpy.Intersect_analysis(inFeatures, intersectOutput)


arcpy.AddField_management(intersectOutput, "AdjustedPop", "DOUBLE")
arcpy.CalculateField_management(intersectOutput, "AdjustedPop", "!" + popField + "! * (!shape.area!/!Area!)", "PYTHON_9.3")
arcpy.AddMessage( "Dissolveing" )
arcpy.Dissolve_management(intersectOutput, dissolveOutput ,["HUC_8"], [["AdjustedPop","SUM"]])


print "Done!"
arcpy.AddMessage( "Done!" )

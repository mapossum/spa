import arcpy

arcpy.env.workspace = r"C:\courses\spa\week6\data\LabData.gdb"
arcpy.env.overwriteOutput = True

inFeatures = "ctracts"
arcpy.AddField_management(inFeatures, "Area", "DOUBLE")
arcpy.CalculateField_management(inFeatures, "Area", "!Shape_Area!", "PYTHON_9.3")

inFeatures = ["ctracts", "watersheds"]
intersectOutput = "CWIntersect"
arcpy.Intersect_analysis(inFeatures, intersectOutput)

arcpy.AddField_management(intersectOutput, "AdjustedPop", "DOUBLE")
arcpy.CalculateField_management(intersectOutput, "AdjustedPop", "!P0010001! * (!Shape_Area!/!Area!)", "PYTHON_9.3")

arcpy.Dissolve_management(intersectOutput, "CWDissolve" ,["HUC_8"], [["AdjustedPop","SUM"]])


print "Done!"

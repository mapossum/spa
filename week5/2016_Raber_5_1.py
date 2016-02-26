import arcpy

arcpy.env.workspace = r"D:\temp\spa\LabData.gdb"
arcpy.env.overwriteOutput = True

inFeatures = "ctracts"
arcpy.AddField_management(inFeatures, "Area", "DOUBLE")
arcpy.CalculateField_management(inFeatures, "Area", "!Shape_Area!", "PYTHON_9.3")

inFeatures = ["ctracts", "watersheds"]
intersectOutput = "CWIntersect"
arcpy.Intersect_analysis(inFeatures, intersectOutput)

arcpy.AddField_management(intersectOutput, "AdjustedPop", "DOUBLE")
arcpy.CalculateField_management(intersectOutput, "AdjustedPop", "!P0010001! * (!Shape_Area!/!Area!)", "PYTHON_9.3")



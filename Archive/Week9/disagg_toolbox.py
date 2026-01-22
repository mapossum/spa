import arcpy

arcpy.env.workspace = r"C:\courses\spa\W6\IntroToArcpy\IntroToArcpy.gdb"

#Inputs

#Feature Class to be disagged
disaggFC = arcpy.GetParameterAsText(2) #"ctracts"
iaFieldName = "Inital_Area"

overlayFC = arcpy.GetParameterAsText(0) #"watersheds"

tintersectFC = "memory\intersect"

oPopFieldName = arcpy.GetParameterAsText(3) #"P0010001"
oUnitsfield = arcpy.GetParameterAsText(1) #"HUC_8"

#Outputs

EstPopFieldName = "Estimated_population"
TotalPopFieldName = "Estimated_population SUM"

disaggoutFC = arcpy.GetParameterAsText(4) #r"disaggdata"

arcpy.management.CalculateField(disaggFC, iaFieldName, "!shape.area!", "PYTHON3", '', "DOUBLE")
arcpy.analysis.PairwiseIntersect("{};{}".format(disaggFC,overlayFC), tintersectFC, "ALL", None, "INPUT")
arcpy.management.CalculateField(tintersectFC, EstPopFieldName, "(!shape.area! / !{}!) * !{}!".format(iaFieldName, oPopFieldName), "PYTHON3", '', "LONG")
arcpy.analysis.PairwiseDissolve(tintersectFC, disaggoutFC, oUnitsfield, TotalPopFieldName, "MULTI_PART")

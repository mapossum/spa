#This is a script that will disagg a field by another field after an intersect.

import arcpy

arcpy.env.workspace = r"C:\courses\spa\W6\IntroToArcpy\IntroToArcpy.gdb"

#Inputs

#Feature Class to be disagged
disaggFC = "ctracts"
iaFieldName = "Inital_Area"

overlayFC = "watersheds"

tintersectFC = "memory\intersect"

oPopFieldName = "P0010001"
oUnitsfield = "HUC_8"

#Outputs

EstPopFieldName = "Estimated_population"
TotalPopFieldName = "Estimated_population SUM"

disaggoutFC = r"disaggdata"

arcpy.management.CalculateField(disaggFC, iaFieldName, "!shape.area!", "PYTHON3", '', "DOUBLE")
arcpy.analysis.PairwiseIntersect("{};{}".format(disaggFC,overlayFC), tintersectFC, "ALL", None, "INPUT")
arcpy.management.CalculateField(tintersectFC, EstPopFieldName, "(!shape.area! / !{}!) * !{}!".format(iaFieldName, oPopFieldName), "PYTHON3", '', "LONG")
arcpy.analysis.PairwiseDissolve(tintersectFC, disaggoutFC, oUnitsfield, TotalPopFieldName, "MULTI_PART")

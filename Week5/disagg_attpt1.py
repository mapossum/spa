import arcpy

arcpy.env.workspace = r'C:\courses\spa\W5\IntroToArcpy\IntroToArcpy.gdb'
arcpy.env.overwriteOutput

inputfeatures = "ctracts"
aggfeatures = "watersheds"

countField = "P0010001"
aggField = "HUC_8"

outputname = "aggregated_input"

arcpy.management.CalculateField(inputfeatures,"InitialArea","!Shape_Area!", field_type="DOUBLE")
arcpy.analysis.PairwiseIntersect([inputfeatures, aggfeatures],"inputs_intersect")
arcpy.management.CalculateField("inputs_intersect","PopEstimate","!{}! * (!Shape_Area! / !InitialArea!)".format(countField), field_type="DOUBLE")
arcpy.analysis.PairwiseDissolve("inputs_intersect", outputname, aggField, "PopEstimate SUM")

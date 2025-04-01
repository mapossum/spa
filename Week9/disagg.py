import arcpy

arcpy.env.overwriteOutput = True

arcpy.env.workspace = "C:\courses\spa\W9\IntroToArcpy\IntroToArcpy.gdb"

#What are the inputs to my process?
PolygonCountData = "ctracts"
CountField = "P0010001"
NewAggregationData = "watersheds"
AggregationField = "HUC_8"
correctedFieldName = "EstimatedPop"

#TempDatasets
intersectData = r"memory\Temporary_Intersect"
intersectInputs = [PolygonCountData, NewAggregationData]

#What are the outputs to my process?
outputDataset = "WatershedSummary"

arcpy.management.AddField(PolygonCountData, "Pre_Area", "DOUBLE", None, None, None, '', "NULLABLE", "NON_REQUIRED", '')
arcpy.management.CalculateField(PolygonCountData, "Pre_Area", "!Shape_Area!", "PYTHON3", '', "TEXT")
arcpy.analysis.Intersect(intersectInputs, intersectData, "ALL", None, "INPUT")
arcpy.management.AddField(intersectData, correctedFieldName, "DOUBLE", None, None, None, '', "NULLABLE", "NON_REQUIRED", '')
arcpy.management.CalculateField(intersectData, correctedFieldName, "!{0}! * (!Shape_Area! / !Pre_Area!)".format(CountField), "PYTHON3", '', "TEXT")
arcpy.management.Dissolve(intersectData, outputDataset, AggregationField, "{0} SUM".format(correctedFieldName), "MULTI_PART", "DISSOLVE_LINES")





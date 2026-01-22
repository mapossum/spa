import arcpy

import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor
import matplotlib
from matplotlib import pyplot as plt

#What are the inputs to my process?
PolygonCountData = arcpy.GetParameterAsText(0)
CountField = arcpy.GetParameterAsText(1)
NewAggregationData = arcpy.GetParameterAsText(2)
AggregationField = arcpy.GetParameterAsText(3)
correctedFieldName = arcpy.GetParameterAsText(5)

#TempDatasets
intersectData = r"memory\Temporary_Intersect"
intersectInputs = [PolygonCountData, NewAggregationData]

#What are the outputs to my process?
outputDataset = arcpy.GetParameterAsText(4)
outputReport = arcpy.GetParameterAsText(6)

arcpy.management.AddField(PolygonCountData, "Pre_Area", "DOUBLE", None, None, None, '', "NULLABLE", "NON_REQUIRED", '')
arcpy.management.CalculateField(PolygonCountData, "Pre_Area", "!Shape_Area!", "PYTHON3", '', "TEXT")
arcpy.analysis.Intersect(intersectInputs, intersectData, "ALL", None, "INPUT")
arcpy.management.AddField(intersectData, correctedFieldName, "DOUBLE", None, None, None, '', "NULLABLE", "NON_REQUIRED", '')
arcpy.management.CalculateField(intersectData, correctedFieldName, "!{0}! * (!Shape_Area! / !Pre_Area!)".format(CountField), "PYTHON3", '', "TEXT")
arcpy.management.Dissolve(intersectData, outputDataset, AggregationField, "{0} SUM".format(correctedFieldName), "MULTI_PART", "DISSOLVE_LINES")


#Put Code here to generate Report
file1 = open(outputReport + r"/report.html","w")
file1.write("This is the report")
file1.close()

arcpy.SetParameterAsText(7, outputReport + r"/report.html")





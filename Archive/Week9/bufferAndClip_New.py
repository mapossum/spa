import arcpy
import numpy as np

input1 = arcpy.GetParameterAsText(0) #r"C:\courses\spa\W9\IntroToArcpy\Ex05\facilities.shp"
input2 = arcpy.GetParameterAsText(1) #r"C:\courses\spa\W9\IntroToArcpy\Ex05\parks.shp"
input1Buffered = "memory/Buffer"
BDist =  arcpy.GetParameterAsText(2) #"300 Meters"
outputdataset = arcpy.GetParameterAsText(3) #r"C:\courses\spa\W9\IntroToArcpy\IntroToArcpy.gdb\parks_Clip3"

arcpy.analysis.Buffer(input1, input1Buffered, BDist, "FULL", "ROUND", "ALL", None, "PLANAR")
arcpy.analysis.Clip(input2, input1Buffered, outputdataset, None)

#Logic to Caluclate the Area of result

#totalArea = 0
#for row in arcpy.da.SearchCursor(outputdataset, ["SHAPE@AREA"]):
#    area = row[0]
#    totalArea = area + totalArea

#Alternative Logic to Caluclate the Area of result
arr = arcpy.da.FeatureClassToNumPyArray(outputdataset, ("Shape_Area"))
totalArea = np.sum(arr["Shape_Area"])


arcpy.SetParameterAsText(4, totalArea)

import arcpy

#arcpy.env.overwriteOutput = True

#This tool finds out the area of one layer (input layer) that is within a specified distance of another layer (overlayLayer)

#Specify Inputs
inputLayer = arcpy.GetParameterAsText(0) #r"G:\courses\spa\W11\IntroToArcpy\Ex05\parks.shp"
overlayLayer = arcpy.GetParameterAsText(1) #r"G:\courses\spa\W11\IntroToArcpy\Ex05\facilities.shp"
miles2Buffer = arcpy.GetParameterAsText(2) #1

#Specify Outputs
ClippedOutputLayer = arcpy.GetParameterAsText(3) #r"G:\courses\spa\W11\IntroToArcpy\Ex05\Outputlayer.shp"

#Specify Temporary Datasets
bufInputLayer = r"memory\Temporary_Buffered"

arcpy.analysis.Buffer(overlayLayer, bufInputLayer, "{0} Miles".format(miles2Buffer), "FULL", "ROUND", "ALL", None, "PLANAR")
arcpy.analysis.Clip(inputLayer, bufInputLayer, ClippedOutputLayer, None)

totalArea = 0
for row in arcpy.da.SearchCursor(ClippedOutputLayer, ["SHAPE@AREA"]):
    area = row[0]
    totalArea = area + totalArea

arcpy.SetParameterAsText(4, totalArea)

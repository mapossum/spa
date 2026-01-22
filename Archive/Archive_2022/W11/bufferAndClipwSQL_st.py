import arcpy

#arcpy.env.overwriteOutput = True

#This tool finds out the area of one layer (input layer) that is within a specified distance of another layer (overlayLayer)

#Specify Inputs
inputLayer = arcpy.GetParameterAsText(0) #r"G:\courses\spa\W11\IntroToArcpy\Ex05\parks.shp"
overlayLayer = arcpy.GetParameterAsText(1) #r"G:\courses\spa\W11\IntroToArcpy\Ex05\facilities.shp"
SQLExpression = arcpy.GetParameterAsText(2)
miles2Buffer = arcpy.GetParameterAsText(3) #1

#Specify Outputs
ClippedOutputLayer = arcpy.GetParameterAsText(4) #r"G:\courses\spa\W11\IntroToArcpy\Ex05\Outputlayer.shp"

#Specify Temporary Datasets
bufInputLayer = r"memory\Temporary_Buffered"
SelectLayer = r"memory\Temporary_Select"

if (SQLExpression != ""):
    arcpy.Select_analysis(overlayLayer, SelectLayer, SQLExpression)
else:
    SelectLayer = overlayLayer
    
arcpy.analysis.Buffer(SelectLayer, bufInputLayer, "{0} Miles".format(miles2Buffer), "FULL", "ROUND", "ALL", None, "PLANAR")
arcpy.analysis.Clip(inputLayer, bufInputLayer, ClippedOutputLayer, None)

totalArea = 0
for row in arcpy.da.SearchCursor(ClippedOutputLayer, ["SHAPE@AREA"]):
    area = row[0]
    totalArea = area + totalArea

arcpy.SetParameterAsText(5, totalArea)

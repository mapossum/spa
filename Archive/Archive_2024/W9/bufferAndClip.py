import arcpy

arcpy.env.overwriteOutput = True

#This tool finds out the area of one layer (input layer) that is within a specified distance of another layer (overlayLayer)

#Specify Inputs
inputLayer = arcpy.GetParameterAsText(0)
overlayLayer = arcpy.GetParameterAsText(1)
miles2Buffer = arcpy.GetParameterAsText(2)

#Specify Outputs
ClippedOutputLayer = arcpy.GetParameterAsText(3)

#Specify Temporary Datasets
bufInputLayer = r"memory\Temporary_Buffered"

arcpy.analysis.Buffer(overlayLayer, bufInputLayer, "{0} Miles".format(miles2Buffer), "FULL", "ROUND", "ALL", None, "PLANAR")
arcpy.analysis.Clip(inputLayer, bufInputLayer, ClippedOutputLayer, None)

#Go through ClippedOutputLayer and total area and report:

fc = ClippedOutputLayer
field = "Shape_Area"
cursor = arcpy.SearchCursor(fc)
totalArea = 0
for row in cursor:
    #arcpy.AddMessage(row.getValue(field))
    totalArea = totalArea + row.getValue(field)

arcpy.SetParameterAsText(4, totalArea)



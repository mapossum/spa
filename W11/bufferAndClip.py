import arcpy

arcpy.env.overwriteOutput = True

#This tool finds out the area of one layer (input layer) that is within a specified distance of another layer (overlayLayer)

#Specify Inputs
inputLayer = r"G:\courses\spa\W11\IntroToArcpy\Ex05\parks.shp"
overlayLayer = r"G:\courses\spa\W11\IntroToArcpy\Ex05\facilities.shp"
miles2Buffer = 1

#Specify Outputs
ClippedOutputLayer = r"G:\courses\spa\W11\IntroToArcpy\Ex05\Outputlayer.shp"

#Specify Temporary Datasets
bufInputLayer = r"memory\Temporary_Buffered"

arcpy.analysis.Buffer(overlayLayer, bufInputLayer, "{0} Miles".format(miles2Buffer), "FULL", "ROUND", "ALL", None, "PLANAR")
arcpy.analysis.Clip(inputLayer, bufInputLayer, ClippedOutputLayer, None)

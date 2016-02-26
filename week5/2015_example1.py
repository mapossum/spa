import arcpy


#List out inputs, outputs, and other intermediate variables

inputWorkspace = r"C:\temp\lab5\labData.gdb"
inputLayer = "taZones"
outputLayer = r"taBuff"
bufferDistance = "500"

arcpy.env.workspace = inputWorkspace
arcpy.env.overwriteOutput = True

desc = arcpy.Describe(inputLayer)

if desc.shapeType <> "Polygon":
    print "This tool only works with Polygon data"
    #Stop Program
else:
    print "Everything is Awesome!"
    #Proceed with Program
    arcpy.Buffer_analysis(inputLayer, outputLayer, bufferDistance, "#", "#", "ALL")

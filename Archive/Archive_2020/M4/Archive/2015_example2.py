import arcpy


#List out inputs, outputs, and other intermediate variables

inputWorkspace = r"C:\temp\lab5\labData.gdb"
arcpy.env.workspace = inputWorkspace
arcpy.env.overwriteOutput = True

datasets = arcpy.ListFeatureClasses()

for inputLayer in datasets:
    outputLayer = inputLayer + "_Buff"
    bufferDistance = "500"

    desc = arcpy.Describe(inputLayer)

    if desc.shapeType <> "Polygon":
        print "This tool only works with Polygon data"
        #Stop Program
    else:
        print "Everything is Awesome!"
        #Proceed with Program
        print inputLayer, outputLayer
        arcpy.Buffer_analysis(inputLayer, outputLayer, bufferDistance, "#", "#", "ALL")

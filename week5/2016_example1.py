import arcpy

arcpy.env.workspace = r"D:\temp\spa\LabData.gdb"
arcpy.env.overwriteOutput = True

inFeatures = ["ctracts", "watersheds"]
outFeatures = "TWUnion"
print "Running Union Analysis"
arcpy.Union_analysis (inFeatures, outFeatures)
print "Finished!"


import arcpy
arcpy.AddMessage(arcpy.env.workspace)

ws = arcpy.env.workspace
if (ws[-4:] <> ".gdb"):
    arcpy.AddMessage("Get Ready for Failure")

#arcpy.env.overwriteOutput = True
#arcpy.env.workspace = r"C:\temp\growthM\labData.gdb"
#workingDir = r"C:\temp\growthM\\"

#GIS data inputs
taZones = arcpy.GetParameterAsText(0)  #"taZones"
taZoneField = arcpy.GetParameterAsText(1)  #"TAZ"

landUse = arcpy.GetParameterAsText(2)  #"landUse"
luField = arcpy.GetParameterAsText(3)  #"LU_Code"
aField = arcpy.GetParameterAsText(4)  #"Acreage"

census = arcpy.GetParameterAsText(5)  #"censusBlocks"
hhField = arcpy.GetParameterAsText(6)  #"Households"
popField = arcpy.GetParameterAsText(7)  #"Population"

#text file inputs
landUseM = arcpy.GetParameterAsText(8)  #workingDir + "landUseMultpliers.txt"
rBO = arcpy.GetParameterAsText(9)  #workingDir + "resBuildOut.csv"
rBOField = arcpy.GetParameterAsText(10)  #"TAZ"

#intermediateDataset
outrBO = "rBOData"
cen_j_taz = "cen_j_taz"
lu_j_taz = "lu_j_taz"
cen_summary = "cen_summary"
lu_summary = "lu_summary"

#outputs
outTaz = arcpy.GetParameterAsText(11)


arcpy.Copy_management(taZones, outTaz)

arcpy.CopyRows_management(rBO, outrBO)

arcpy.JoinField_management(outTaz, taZoneField, outrBO, rBOField)

arcpy.SpatialJoin_analysis(census, taZones, cen_j_taz, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "HAVE_THEIR_CENTER_IN")

arcpy.Statistics_analysis(cen_j_taz, cen_summary, [[popField, "SUM"],[hhField, "SUM"]], taZoneField)

arcpy.JoinField_management(outTaz, taZoneField, cen_summary, taZoneField)

arcpy.AddField_management(outTaz, "PGM", "DOUBLE")

codeblock = "def findtotal(a,b):\n  if b >0:\n    return a / b\n  else:\n    return 0"

arcpy.CalculateField_management(outTaz, "PGM", 'findtotal( !SUM_' + popField + '!, !SUM_' + hhField + '!)', "PYTHON_9.3" , codeblock)

#Spatial Join on LandUse with TAZ
arcpy.SpatialJoin_analysis(landUse, taZones, lu_j_taz, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "HAVE_THEIR_CENTER_IN")

arcpy.Statistics_analysis(lu_j_taz, lu_summary, [[aField, "SUM"]], [taZoneField,luField])

f = open(landUseM, 'r')

for line in f:
    lu = line.strip()
    landUseData = lu.split("\t")
    print landUseData

    arcpy.TableSelect_analysis(lu_summary, lu_summary + "_" + landUseData[0], luField + " = '" + landUseData[0] + "'")

    arcpy.AddField_management(lu_summary + "_" + landUseData[0], landUseData[0] + "_A", "DOUBLE")
    arcpy.CalculateField_management(lu_summary + "_" + landUseData[0], landUseData[0] + "_A", "!SUM_" + aField + "!", "PYTHON_9.3")
    arcpy.DeleteField_management(lu_summary + "_" + landUseData[0], ["SUM_" + aField, "FREQUENCY"])
    

    #Join each output back to TazDataset (outTaz)
    arcpy.JoinField_management(outTaz, taZoneField, lu_summary + "_" + landUseData[0], taZoneField)

    #Join each output back to TazDataset (outTaz)
    #Add the field(s) you need
    #Calculate The final fields

#one more field calc
    

f.close()

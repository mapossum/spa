
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\temp\growthM\labData.gdb"
workingDir = r"C:\temp\growthM\\"

#GIS data inputs
taZones = "taZones"
landUse = "landUse"
census = "censusBlocks"

#text file inputs
landUseM = workingDir + "landUseMultpliers.txt"
rBO = workingDir + "resBuildOut.csv"

#intermediateDataset
outrBO = "rBOData"
cen_j_taz = "cen_j_taz"
lu_j_taz = "lu_j_taz"
cen_summary = "cen_summary"
lu_summary = "lu_summary"

#outputs
outTaz = "outTaz"


arcpy.Copy_management(taZones, outTaz)

arcpy.CopyRows_management(rBO, outrBO)

arcpy.JoinField_management(outTaz, "TAZ", outrBO, "TAZ")

arcpy.SpatialJoin_analysis(census, taZones, cen_j_taz, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "HAVE_THEIR_CENTER_IN")

arcpy.Statistics_analysis(cen_j_taz, cen_summary, [["Population", "SUM"],["Households", "SUM"]], "TAZ")

arcpy.JoinField_management(outTaz, "TAZ", cen_summary, "TAZ")

arcpy.AddField_management(outTaz, "PGM", "DOUBLE")

codeblock = "def findtotal(a,b):\n  if b >0:\n    return a / b\n  else:\n    return 0"

arcpy.CalculateField_management(outTaz, "PGM", 'findtotal( !SUM_Population!, !SUM_Households!)', "PYTHON_9.3" , codeblock)

#Spatial Join on LandUse with TAZ
arcpy.SpatialJoin_analysis(landUse, taZones, lu_j_taz, "JOIN_ONE_TO_MANY", "KEEP_COMMON", "#", "HAVE_THEIR_CENTER_IN")

arcpy.Statistics_analysis(lu_j_taz, lu_summary, [["Acreage", "SUM"]], ["TAZ","LU_Code"])

f = open(landUseM, 'r')

for line in f:
    lu = line.strip()
    landUseData = lu.split("\t")
    print landUseData

    arcpy.TableSelect_analysis(lu_summary, lu_summary + "_" + landUseData[0], "LU_Code = '" + landUseData[0] + "'")

    #Join each output back to TazDataset (outTaz)
    #Add the field(s) you need
    #Calculate The final fields

#one more field calc
    

f.close()

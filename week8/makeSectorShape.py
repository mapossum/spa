import os
from math import sin, cos, radians, pi
def point_pos(x0, y0, d, theta):
    theta_rad = pi/2 - radians(theta)
    return x0 + d*cos(theta_rad), y0 + d*sin(theta_rad)


import arcpy
arcpy.env.overwriteOutput = True

#Inputs
inputDataset = arcpy.GetParameterAsText(0) #r"C:\temp\Cityi10.shp"

centerF = arcpy.GetParameterAsText(1) #"index"
fieldList = arcpy.GetParameterAsText(2)
allFields = fieldList.split(";")
#allFields = ["Fish","Coral","Commerical","Fleshy"]

rotationAngle = 360 / len(allFields)

innerSize = float(arcpy.GetParameterAsText(3)) #1000
outerSize = float(arcpy.GetParameterAsText(4)) #2000

FieldType = arcpy.GetParameterAsText(5) # "LONG"

#Outputs
outputDataset = arcpy.GetParameterAsText(6)

saveSeperate = arcpy.GetParameter(7)

outputFolder = os.path.dirname(outputDataset) #r"C:/temp/"
outputName = os.path.basename(outputDataset) #"Output.shp"

if (outputName[-4:] == ".shp"):
    ending = ".shp"
else:
    ending = ""

arcpy.CreateFeatureclass_management(outputFolder, outputName, "POLYGON", inputDataset, "DISABLED", "DISABLED", inputDataset)

field_list = arcpy.ListFields(outputDataset)

arcpy.AddField_management(outputDataset, "Field", "TEXT")
arcpy.AddField_management(outputDataset, "Value", FieldType)

delfields = []
for flds in field_list:
    if not ((flds.type == "Geometry") or (flds.type == "OID") or (flds.name == "Shape_Area") or (flds.name == "Shape_Length")):
        delfields.append(flds.name)

arcpy.DeleteField_management(outputDataset, delfields)


outCursor = arcpy.da.InsertCursor(outputDataset,("Field", "Value", "SHAPE@"))


allFields.append(centerF)
allFields.append("SHAPE@XY")


with arcpy.da.SearchCursor(inputDataset, allFields) as cursor:
    for row in cursor:
        pT = row[-1]
        point = arcpy.Point(*pT)
        ptGeometry = arcpy.PointGeometry(point)

        outCenter = ptGeometry.buffer(outerSize)
        inCenter = ptGeometry.buffer(innerSize)


        for x in range(0,len(allFields)-2):

            cliperF = [row[-1]]
            sAngle = x * rotationAngle
            eAngle = (x+1) * rotationAngle
            cliperF.append(point_pos(pT[0],pT[1],outerSize * 2,sAngle))
            cliperF.append(point_pos(pT[0],pT[1],outerSize * 2,eAngle))
            clipperG = arcpy.Polygon(arcpy.Array([arcpy.Point(*coords) for coords in cliperF]))
            sectorG = clipperG.intersect(outCenter,4)
            outG = sectorG.difference(inCenter)
            outRow = (allFields[x], row[x], outG)
            outCursor.insertRow(outRow)

        outRow = (allFields[-2], row[-2], inCenter)
        outCursor.insertRow(outRow)

del cursor, outCursor

if (saveSeperate):
    for x in range(0,len(allFields)-1):
        arcpy.AddMessage("Processing: " + allFields[x])
        arcpy.Select_analysis(outputDataset, outputFolder + "\\" + allFields[x] + ending, '"Field" = ' + "'" + allFields[x] + "'")
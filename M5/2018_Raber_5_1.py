import arcpy


arcpy.env.workspace = r"C:\temp\LabData.gdb"
arcpy.env.overwriteOutput = True

inData = "ctracts"
oAreaField = "Orig_Area"

#Add field to ctracts to store Org Area
arcpy.AddField_management(inData, oAreaField, "DOUBLE")

#Caculate Field to store Orig Area

arcpy.CalculateField_management(inData, oAreaField, "!Shape_Area!", "PYTHON")

#Intersect ctract and watersheds

#add new field for new pop

#calculate new pop (oldpop * newarea/oldarea)

#dissolve based on watershed

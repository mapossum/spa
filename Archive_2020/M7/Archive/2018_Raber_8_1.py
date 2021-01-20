import arcpy, SEC

arcpy.env.workspace = r"C:\temp\spaLab\week8"
fc = r'Cityi10.shp'


#ADD Three Fields to input shapefile

arcpy.AddField_management(fc, "PARA", "DOUBLE")
arcpy.AddField_management(fc, "SSQR", "DOUBLE")
arcpy.AddField_management(fc, "SCIRCLE", "DOUBLE")

fields = ['PARA', 'SSQR', 'SCIRCLE', 'Name10', 'SHAPE@AREA', 'SHAPE@LENGTH', 'SHAPE@']

cursor = arcpy.da.UpdateCursor(fc, fields)
for row in cursor:
    row[0] = row[5] / row[4]
    row[1] = row[0] / (row[4]**0.5 / row[4])
    #row[2] = row[0] / 
    cursor.updateRow(row)
    points = []
    for part in row[6]:
        for pt in part:
            print pt
            points.append((pt.X, pt.Y))
    
print "JOB COMPLETE!"
    

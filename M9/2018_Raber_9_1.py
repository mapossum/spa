import arcpy, SEC

arcpy.env.workspace = r"C:\temp\spaLab\week8"
pfc = r'Cityi10Simple.shp'
fc = r'Cityi10Simple_out.shp'

#Create a second Shapefile using fc as a template
arcpy.Copy_management(pfc, fc)

arcpy.AddField_management(fc, "PARA", "DOUBLE")
arcpy.AddField_management(fc, "SSQR", "DOUBLE")
arcpy.AddField_management(fc, "SCIRCLE", "DOUBLE")
arcpy.AddField_management(fc, "CSTAT", "DOUBLE")

fields = ['PARA', 'SSQR', 'SCIRCLE', 'Name10', 'SHAPE@AREA', 'SHAPE@LENGTH', 'SHAPE@', 'CSTAT']

cursor = arcpy.da.UpdateCursor(fc, fields)
for row in cursor:
    row[0] = row[5] / row[4]
    row[1] = row[0] / (row[4]**0.5 / row[4])
    #row[2] = row[0] / 
    points = []
    for part in row[6]:
        try:
            for pt in part:
                inputpoint = (pt.X, pt.Y)
                points.append(inputpoint)
        except:
            print "Empty Part"
    try:
        mbc = SEC.make_circle(points)
        point = arcpy.Point(mbc[0], mbc[1])
        newpolygon = arcpy.PointGeometry(point).buffer(mbc[2])
        cstat = row[4] / newpolygon.area
        print row[3], mbc, cstat
        row[7] = cstat
        #This is a line you need to add
        row[6] = newpolygon
    except:
        print "Bad City: " + row[3]
    cursor.updateRow(row)
    
print "JOB COMPLETE!"
    

import arcpy
import math
import SEC

arcpy.env.overwriteOutput = True

fc = r"C:\temp\Cityi10.shp"
fc2 = r"C:\temp\Cityi10_copy.shp"

arcpy.Copy_management(fc, fc2)

#add 3 new fields
arcpy.AddField_management(fc2, "PARA", "DOUBLE")
arcpy.AddField_management(fc2, "SHAPE_1", "DOUBLE")
arcpy.AddField_management(fc2, "SCIRCLE", "DOUBLE")
arcpy.AddField_management(fc2, "CCIRCLE", "DOUBLE")

fields = ["Name10", "SHAPE@", "PARA", "SHAPE_1", "SCIRCLE", "CCIRCLE"]

# loop through each city and field shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:
        print row[0], row[1].getLength()
        perim = row[1].getLength()
        area = row[1].getArea()
        ptoa = perim / area

        sqside = math.sqrt(area)
        shapeindex = ((sqside * 4) / area) / ptoa
        cperim = math.sqrt(area / math.pi) * 2 * math.pi
        scircle = (cperim / perim)


        pointList = []
        # calculate ccircle
        buf = row[1].buffer(0.01)
        for part in buf:
            for coord in part:
                try:
                    pointList.append((coord.X, coord.Y))
                except:
                    print "bad point"
        
        c = SEC.make_circle(pointList)
        circlearea = math.pi * c[2] * c[2]
        ccircle = area / circlearea
        print ptoa, shapeindex, scircle, ccircle

        cp = arcpy.PointGeometry(arcpy.Point(c[0], c[1]))
        
        polygonbuf = cp.buffer(c[2])
        row[1] = polygonbuf
        row[2] = ptoa
        row[3] = shapeindex
        row[4] = scircle
        row[5] = ccircle
        
        cursor.updateRow(row)

    

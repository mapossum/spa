import arcpy
import math
import SEC

arcpy.env.overwriteOutput = True

fc = r"C:\temp\Cityi10.shp"
fc2 = r"C:\temp\Cityi10_copy.shp"

arcpy.Copy_management(fc, fc2)

#add four new fields to fc2??

arcpy.AddField_management(fc2, "PARA", "DOUBLE")
arcpy.AddField_management(fc2, "SHAPE_I", "DOUBLE")
arcpy.AddField_management(fc2, "CIRCLE", "DOUBLE")
arcpy.AddField_management(fc2, "SCIRCLE", "DOUBLE")

fields = ["Name10", "SHAPE@", "PARA", "SHAPE_I", "CIRCLE", "SCIRCLE"]

#loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:
        print row[0], row[1].getLength()
        perimeter = row[1].getLength()
        area = row[1].getArea()
        ptoa = perimeter / area
        

        sqside = math.sqrt(area)
        shapeindex= ((sqside * 4) / area) / ptoa
        cperimeter = math.sqrt(area / math.pi) * 2 * math.pi
        scircle = (cperimeter / perimeter)

        pointList = []
        #calculate circle
        buf = row[1].buffer(0.01)
        for part in buf:
            for coord in part:
                try:
                    pointList.append((coord.X, coord.Y))
                except:
                    print "Bad Point"
                    
                

        c = SEC.make_circle(pointList)
        print c
        circlearea = math.pi * c[2] * c[2]
        ccircle = area / circlearea
        print ptoa, shapeindex, scircle, ccircle

        cp = arcpy.PointGeometry(arcpy.Point(c[0],c[1]))

        polygonbuf = row[1].buffer(100)
        row[1] = polygonbuf.difference(row[1])
        row[2] = ptoa
        row[3] = shapeindex
        row[4] = ccircle
        row[5] = scircle
        cursor.updateRow(row)


import arcpy
import math
import SEC

arcpy.env.overwriteOutput = True

fc = r"C:\temp\Cityi10.shp"
fc2 = r"C:\temp\Cityi10_copy.shp"

arcpy.Copy_management(fc, fc2)

#add four new fields to fc2???

arcpy.AddField_management(fc2, "PARA", "DOUBLE")

fields = ["Name10", "SHAPE@", "PARA"]  #<<--add the other fields that you just created

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
        scircle =  cperim / perim

        pointList = []
        #calculate ccircle
        buf = row[1].buffer(0.01)
        for part in buf:
            for coord in part:
                try:
                    pointList.append( (coord.X, coord.Y) )
                except:
                    print "bad point"
                
        c = SEC.make_circle(pointList)
        circlearea = math.pi * c[2] * c[2]
        ccircle = area / circlearea
        print ptoa, shapeindex, scircle, ccircle

        cp = arcpy.PointGeometry(arcpy.Point(c[0], c[1]))
        print c
        polygonbuf = cp.buffer(c[2])
        row[1] = polygonbuf
        row[2] = ptoa
        # Three more times
        cursor.updateRow(row)
    

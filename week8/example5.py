import arcpy, SEC

arcpy.env.overwriteOutput = True

fc = r"C:\temp\week8\Cityi10.shp"
fc2 = r"C:\temp\week8\Cityi10_copy2.shp"

arcpy.Copy_management(fc, fc2)

fields = ["Name10", "SHAPE@"]

# loop through each city and find shape
with arcpy.da.UpdateCursor(fc2, fields) as cursor:
    for row in cursor:
        partnum = 0
        # Step through each part of the feature
        #
        points = []
        geo = row[1].buffer(0.005)
        for part in geo:
            # Print the part number
            #
            #print("Part {0}:".format(partnum))

            # Step through each vertex in the feature
            #
            for pnt in part:
                if pnt:
                    # Print x,y coordinates of current point
                    #
                    points.append((pnt.X, pnt.Y))
                    #print("{0}, {1}".format(pnt.X, pnt.Y))
                else:
                    # If pnt is None, this represents an interior ring
                    #
                    pass
                    #print("Interior Ring:")
            partnum += 1
        try:

            circledef = SEC.make_circle(points)
            cp = arcpy.PointGeometry(arcpy.Point(circledef[0], circledef[1]))
            scc = cp.buffer(circledef[2])
            #HOW TO CALCULATE???
            CIRCLE = geo.area / scc.area
            print row[0], CIRCLE
            row[1] = scc
            cursor.updateRow(row)

        except:
            print row[0] + " Did not work"
        

del cursor, row

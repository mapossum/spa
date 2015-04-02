import arcpy, SEC, math

arcpy.env.overwriteOutput = True

fc = r"C:\temp\week8\Cityi10.shp"
fc2 = r"C:\temp\week8\Cityi10_copy.shp"


arcpy.Copy_management(fc, fc2)

fc3 = arcpy.CreateFeatureclass_management(r"C:\temp\week8" , "circledif_copy2.shp", "POLYGON", "#", "#", "#", fc)
fc4 = arcpy.CreateFeatureclass_management(r"C:\temp\week8" , "circle.shp", "POLYGON", "#", "#", "#", fc)                                    

arcpy.AddField_management(fc2, "PARA", "DOUBLE")
arcpy.AddField_management(fc2, "SHAPE_I", "DOUBLE")
arcpy.AddField_management(fc2, "CIRCLE", "DOUBLE")
arcpy.AddField_management(fc2, "SCIRCLE", "DOUBLE")

arcpy.AddField_management(fc3, "Name10", "TEXT")
arcpy.AddField_management(fc3, "PARA", "DOUBLE")
arcpy.AddField_management(fc3, "SHAPE_I", "DOUBLE")
arcpy.AddField_management(fc3, "CIRCLE", "DOUBLE")
arcpy.AddField_management(fc3, "SCIRCLE", "DOUBLE")

arcpy.AddField_management(fc4, "Name10", "TEXT")
arcpy.AddField_management(fc4, "PARA", "DOUBLE")
arcpy.AddField_management(fc4, "SHAPE_I", "DOUBLE")
arcpy.AddField_management(fc4, "CIRCLE", "DOUBLE")
arcpy.AddField_management(fc4, "SCIRCLE", "DOUBLE")


fields = ["Name10", "SHAPE@", "PARA", "SHAPE_I", "CIRCLE", "SCIRCLE"]

cursor_cir_dif = arcpy.da.InsertCursor(fc3, ['Name10','SHAPE@',"PARA", "SHAPE_I", "CIRCLE", "SCIRCLE"])
cursor_cir = arcpy.da.InsertCursor(fc4, ['Name10','SHAPE@',"PARA", "SHAPE_I", "CIRCLE", "SCIRCLE"])
# loop through each city and find shape
cursor = arcpy.da.UpdateCursor(fc2, fields)

    
    # Step through each part of the feature
    #
def get_points(row):
    geo = row[1].buffer(0.005)
    partnum = 0
    points = []
    
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
        return points
    
for row in cursor:
    geo1 = row[1].buffer(0.005)
    points = get_points(row)
    
    
    circledef = SEC.make_circle(points)
    print circledef
    cp = arcpy.PointGeometry(arcpy.Point(circledef[0], circledef[1]))
    scc = cp.buffer(circledef[2])
    
    #HOW TO CALCULATE???
    CIRCLE = geo1.area / scc.area
    PARA = geo1.length / geo1.area
    SHAPE_I = PARA / ((math.sqrt(geo1.area)*4)/geo1.area)
    RAD = math.sqrt(geo1.area/math.pi)
    SCIRCLE = geo1.length / (2*math.pi*RAD)
    
    row[2] = PARA
    row[3] = SHAPE_I
    row[4] = CIRCLE
    row[5] = SCIRCLE
    cursor.updateRow(row)
         
    dif = scc.difference(geo1)
    row[1] = scc
    cursor_cir_dif.insertRow(row)


    print row[0] + " Did not work (second part)"
        



    
    
del cursor, row, cursor_cir, cursor_cir_dif

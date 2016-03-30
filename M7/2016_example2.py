import arcpy

fc = r"C:\temp\m7\Cityi10.shp"
fields = ["SHAPE@", "NAME10", 'ALAND10']

# For each row print the WELL_ID and WELL_TYPE fields, and the
#  the feature's x,y coordinates
#
#with arcpy.da.SearchCursor(fc, fields) as cursor:
#    for row in cursor:
#        print("{0}, {1}, {2}".format(row[0], row[1], row[2]))


cursor = arcpy.da.SearchCursor(fc, fields)

for row in cursor:
    shape = row[0]
    for part in shape:
        print part, row[1]
        print part[0]
        for coord in part:
            #print coord
            pass
    #print row[0], row[1]

del cursor, row

import arcpy

arcpy.env.workspace = r"C:\temp\spaLab\week8"
fc = r'Cityi10.shp'
fields = ['Name10', 'SHAPE@']

cursor = arcpy.da.SearchCursor(fc, fields)
for row in cursor:
    if (row[1].partCount > 1):
        print('Town Name: {0}, Parts: {1}, Points: {2}'.format(row[0], row[1].partCount, row[1].pointCount))
        for part in row[1]:
            print part
            for point in part:
                print point
    #print row[0], row[1].partCount, row[1].pointCount

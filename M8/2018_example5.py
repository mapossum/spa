import arcpy

arcpy.env.workspace = r"C:\temp\spaLab\week8"
fc = r'Cityi10.shp'
fields = ['Name10', 'SHAPE@']

cursor = arcpy.da.SearchCursor(fc, fields, "Name10 LIKE 'G%'")
for row in cursor:
    print('Town Name: {0}, Parts: {1}, Points: {2}'.format(row[0], row[1].partCount, row[1].pointCount))
    #print row[0], row[1].partCount, row[1].pointCount
